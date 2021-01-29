#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tommaso Caselli
#
# This program re-uses some code from Genre Classifier - 2016 Juliette Lonij, Koninklijke Bibliotheek
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import numpy as np
import sys, re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.svm import LinearSVC, SVC
from sklearn.model_selection import GridSearchCV
from nltk.corpus import stopwords
from sklearn.metrics import classification_report, confusion_matrix
import csv
import emoji

def validate(Xtrain,Ytrain,task_type):

    """
    :param Xtrain: train messages
    :param Ytrain: labels train
    :return:
    """

    """
    Grid search hyper-param tuning
    """


    svm_classifier = SVC(kernel='linear')

    # unweighted word uni and bigrams
    count_word = TfidfVectorizer(ngram_range=(1,2), stop_words=stopwords.words('dutch'))
    count_char = TfidfVectorizer(analyzer='char', ngram_range=(2,5))


    text_features = FeatureUnion([('word', count_word),
                                  ('char', count_char),
                                  ])

    pipeline_svm = Pipeline([("features", text_features), ("svm", svm_classifier)])

    print("Running grid search for tuning SVM...")

    clf_grid_svm = GridSearchCV(pipeline_svm,
                                param_grid={'svm__C': [0.1, 1.0, 10.0, 100.0]},
                                cv=10,
                                scoring='f1_macro')

    clf_grid_svm.fit(Xtrain, Ytrain)

    print("Best parameters for SVM:")
    print("\n")
    print(clf_grid_svm.best_params_)

    print("Best scores")
    print("\n")
    means = clf_grid_svm.cv_results_['mean_test_score']
    stds = clf_grid_svm.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf_grid_svm.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r" % (mean, std * 2, params))
    print("\n")


def train(Xtrain, Ytrain, x_dev,y_gold,task_type):

    # Train and test on dev and evaluate

    svm_classifier = SVC(kernel='linear', C=1.0)

    # unweighted word uni and bigrams
    count_word = TfidfVectorizer(ngram_range=(1, 2), stop_words=stopwords.words('dutch'))
    count_char = TfidfVectorizer(analyzer='char', ngram_range=(2, 5))

    text_features = FeatureUnion([('word', count_word),
                                  ('char', count_char),
                                  ])

    pipeline_svm = Pipeline([("features", text_features), ("svm", svm_classifier)])

    pipeline_svm.fit(Xtrain, Ytrain)

    print('Predicting on validation...')
    Yguess = pipeline_svm.predict(x_dev) # dev or test data
    print(classification_report(y_gold, Yguess))
    print(confusion_matrix(y_gold, Yguess))



def read_corpus(inputf,binary=True):

    tweets = []
    labels = []

    with open(inputf, newline='') as csvfile:
        read_data = csv.reader(csvfile, delimiter='\t',) # dalc 2.0
        next(read_data) # dalc 2.0 test
        for row in read_data:
            # store messages
            tweets.append(row[1])
            if binary:
                # 2-class problem: ABU vs. NOT
                labels.append(row[4].replace('EXPLICIT', 'ABU').replace('IMPLICIT', 'ABU'))
            else:
                # 3-class problem: NOT, EXPLICIT, IMPLICIT
                labels.append(row[4])

        return tweets, labels

def clean_samples(samples):

    new_samples = []
    for tweet_message in samples:
        # only removing the hash # sign from the word
        #tweet_message = re.sub(r'#', '', tweet_message)

        tweet_message = re.sub(r'https.*[^ ]', 'URL', tweet_message)
        tweet_message = re.sub(r'http.*[^ ]', 'URL', tweet_message)
        tweet_message = re.sub(r'@([^ ]*)', '@USER', tweet_message)
        tweet_message = emoji.demojize(tweet_message)
        tweet_message = re.sub(r'(:.*?:)', r' \1 ', tweet_message)
        tweet_message = re.sub(' +', ' ', tweet_message)
        new_samples.append(tweet_message)

    return new_samples


def training_data(inputtr,inputdev,task_type):

    print("Reading train and dev ...")

    if task_type == 'binary':
        Xtrain, Ytrain = read_corpus(inputtr)
        x_dev, y_gold = read_corpus(inputdev)
    else:
        Xtrain, Ytrain = read_corpus(inputtr, binary=False)
        x_dev, y_gold = read_corpus(inputdev, binary=False)

    # Minimal preprocessing / cleaning
    Xtrain = clean_samples(Xtrain)
    x_dev = clean_samples(x_dev)

    #validate(Xtrain,Ytrain,task_type)
    train(Xtrain, Ytrain, x_dev,y_gold, task_type)

if __name__ == '__main__':

    """
    Usage: python3* grid_search_svm.py [training_file] [dev_file]
    - select validate in training_data() to run grid search
    - select train in training_data() to train, test, and dump models with optimzed parameters

    """

    training_set = sys.argv[1]
    dev_set = sys.argv[2] # dev or test data
    task_type = sys.argv[3] # values are binary or multi

    training_data(training_set,dev_set,task_type)
