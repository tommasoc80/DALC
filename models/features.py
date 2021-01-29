'''
This is a file containing features we can incorporate into the SVM models
Import this file (or individual objects from this file) as modules
'''

import re
import statistics as stats
import json
import nltk, csv
from nltk.stem.snowball import SnowballStemmer

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.base import BaseEstimator, TransformerMixin

from scipy.sparse import csr_matrix



class Embeddings(TransformerMixin):
    '''Transformer object turning a sentence (or tweet) into a single embedding vector'''

    def __init__(self, word_embeds, pool='average'):
        '''
        Required input: word embeddings stored in dict structure available for look-up
        pool: sentence embeddings to be obtained either via average pooling ('average') or max pooing ('max') from word embeddings. Default is average pooling.
        '''
        self.word_embeds = word_embeds
        self.pool_method = pool

    def transform(self, X, **transform_params):
        '''
        Transformation function: X is list of sentence/tweet - strings in the train data. Returns list of embeddings, each embedding representing one tweet
        '''
        return [self.get_sent_embedding(sent, self.word_embeds, self.pool_method) for sent in X]

    def fit(self, X, y=None, **fit_params):
        return self

    def get_sent_embedding(self, sentence, word_embeds, pool):
        '''
        Obtains sentence embedding representing a whole sentence / tweet
        '''
        # simply get dim of embeddings
        l_vector = len(word_embeds['und'])

        # replace each word in sentence with its embedding representation via look up in the embedding dict strcuture
        # if no word_embedding available for a word, just ignore the word
        # [[0.234234,-0.276583...][0.2343, -0.7356354, 0.123 ...][0.2344356, 0.12477...]...]
        list_of_embeddings = [word_embeds[word.lower()] for word in sentence.split() if word.lower() in word_embeds]

	    # Obtain sentence embeddings either by average or max pooling on word embeddings of the sentence
        # Option via argument 'pool'
        if pool == 'average':
            sent_embedding = [sum(col) / float(len(col)) for col in zip(*list_of_embeddings)]  # average pooling
        elif pool == 'max':
            sent_embedding = [max(col) for col in zip(*list_of_embeddings)]	# max pooling
        else:
            raise ValueError('Unknown pooling method!')

        # Below case should technically not occur
        if len(sent_embedding) != l_vector:
            sent_embedding = [0] * l_vector

        return sent_embedding


class Lexicon(TransformerMixin):
    '''
    Feature extractor converting each sample to number of bad words it contains normalised by its length
    Bad word list is passed in as positional argument of class object
    '''

    def __init__(self, word_file):
        ''' required input: file with list of bad words '''
        self.word_file = word_file

    def fit(self, x, y=None):
        return self

    def _get_features(self, tweet):
        '''check if twitter tokens are in a list of 'bad' words'''

        with open(self.word_file, 'r',encoding='latin-1') as fi:
            bad_list = fi.read().strip().split()

        with open(self.word_file, 'r') as f:  # GROFLEX
            read_lexicon = csv.reader(f, delimiter='\t', )  # GROFLEX
            next(read_lexicon)
            for row in read_lexicon:
                bad_list = row[3].strip().split()

        tokens = nltk.word_tokenize(tweet)

        stemmer = SnowballStemmer("dutch")
        stemmed_tokens = [stemmer.stem(entry) for entry in tokens]

        len_tok = len(tokens)
        count = 0
        for token in stemmed_tokens:
            if token in bad_list:
                count += 1
        how_bad = count/len_tok
        return round(how_bad,2)

    def transform(self, tweets):
        values = csr_matrix([self._get_features(tweet) for tweet in tweets])
        return csr_matrix.transpose(values)


class TweetLength(BaseEstimator, TransformerMixin):
    """
    Transformer which turns each input sample into its length in terms of number of characters
    """

    def __init__(self):
        pass

    def fit(self, X, y=None, **fit_params):
        return self

    def transform(self, X, **transform_params):
        ''' Just get length over the whole tweet string '''

        # Desired output: matrix where axis 0 = n_sample
        values = csr_matrix([len(tweet) for tweet in X])
        return csr_matrix.transpose(values)





###### Testing these classes ##################################################

if __name__ == '__main__':

    from sklearn.feature_extraction import DictVectorizer
    from sklearn.pipeline import Pipeline, FeatureUnion
    import gensim.models as gm

    tweets = []
    with open('../dalc_v2_train.csv', 'r', encoding='utf-8') as fi:
        read_data = csv.reader(fi, delimiter='\t', )  # dalc 2.0 test
        next(read_data)  # dalc 2.0 test
        for row in read_data:
            tweet_id = row[0]
            message = row[1]
            labels = row[4].replace('EXPLICIT', 'ABU').replace('IMPLICIT', 'ABU')

            tweets.append(message)

    print('len(tweets):', len(tweets))
    # vec_badwords = Pipeline([('badness', BadWords('lexicon.txt')), ('vec', DictVectorizer())])
    vec_lexicon = Lexicon('groflex.tsv')
    Xlex = vec_lexicon.fit_transform(tweets)
    print(type(Xlex))
    print(Xlex.shape)
    print(tweets[30:40])
    print('hello')
    print(Xlex[30:40])

    print()

    vec_len = TweetLength()
    Xlen = vec_len.fit_transform(tweets)
    print(type(Xlen))
    print(Xlen.shape)
    print(tweets[30:40])
    print(Xlen[30:40])

    '''
    embeddings = gm.KeyedVectors.load('../../Resources/hate_german.bin').wv
    print('Finished getting embeddings')
    vec_emb = Embeddings(embeddings, pool='max')
    print(vec_emb.pool_method)
    Xemb = vec_emb.fit_transform(tweets)
    # print(len(Xemb))
    # print(len(Xemb[0]))
    # print(Xemb[:2])

    count_word = CountVectorizer(ngram_range=(1,2))
    count_char = CountVectorizer(analyzer='char', ngram_range=(3,4))

    vectorizer = FeatureUnion([('word', count_word),
                                ('char', count_char),
                                ('badwords', vec_badwords),
                                ('tweetlen', TweetLength()),
                                ('word_embeds', vec_emb)])
    X = vectorizer.fit_transform(tweets)
    print(type(X))
    print(X.shape)

    '''








############### Space ####
