import csv, re
from nltk.stem.snowball import SnowballStemmer
import spacy
import emoji
from sklearn.metrics import classification_report, confusion_matrix

nl_ = spacy.load('nl_core_news_sm')

def output_print(prediction_list, outfile_):

    output = open(outfile_, "a")

    for entry in prediction_list:
        id, label = entry
        output.writelines(id + "," + label + "\n")
    output.close()


def check_messages(message_dict, offensive_term,message_ids):
    offensive = set()

    classified_elems = {}
    prediction_out = []

    for id, tokenized_message in message_dict.items():
        for elem in tokenized_message:
            if elem in offensive_term:
                #print(elem)
                offensive.add(id)

    for elem in offensive:
        classified_elems[elem] = "ABU"

    for id, tokenized_message in message_dict.items():
        if id not in classified_elems:
            classified_elems[id] = "NOT"

# order the ids as in the input test file

    for elem in message_ids:
        match = (elem, classified_elems[elem])
        prediction_out.append(match)

    return prediction_out


def clean_tokens(tweet_message):

    tweets_clean = []

    # only removing the hash # sign from the word
    tweet_message = re.sub(r'#', '', tweet_message)

    tweet_message = re.sub(r'https.*[^ ]', 'URL', tweet_message)
    tweet_message = re.sub(r'http.*[^ ]', 'URL', tweet_message)
    tweet_message = re.sub(r'@([^ ]*)', '@USER', tweet_message)
    tweet_message = emoji.demojize(tweet_message)
    tweet_message = re.sub(r'(:.*?:)', r' \1 ', tweet_message)
    tweet_message = re.sub(' +', ' ', tweet_message)

    # tokenize
    doc = nl_(tweet_message)
    tokens = [token.text.lower() for token in doc]

    # get stem of tokens
    for elem in tokens:
        stem_token = SnowballStemmer('dutch').stem(elem) # stemming word
        tweets_clean.append(stem_token)

    return tweets_clean
    #return tokens


def read_and_match(comments, lexicon):

    tokens_ = {}
    message_ids = []
    gold_labels = []

    with open(comments, newline='') as csvfile:
        read_data = csv.reader(csvfile, delimiter='\t',) # dalc 2.0 test
        next(read_data) # dalc 2.0 test
        for row in read_data:
            tweet_id = row[0]
            message = row[1]
            labels = row[4].replace('EXPLICIT', 'ABU').replace('IMPLICIT', 'ABU')
            #if labels == "":
            #    print(tweet_id)

            gold_labels.append(labels)
            message_ids.append(tweet_id)

            """
            tokenize data and clean it
            """
            tokens = clean_tokens(message)
            tokens_[tweet_id] = tokens

#    print(len(gold_labels))
#    print(list(set(gold_labels)))

    abusive_list = []

    with open(lexicon) as f:  # GROFLEX
        read_lexicon = csv.reader(f, delimiter='\t', )  # GROFLEX
        next(read_lexicon)
        for row in read_lexicon:

            stem_abusive = SnowballStemmer('dutch').stem(row[3])
            abusive_list.append(stem_abusive)


    print("number of test messages: " + str(len(tokens_))) # number of messages

    set_1 = check_messages(tokens_, abusive_list,message_ids)

    most_freq_baseline = []

    for elem in message_ids:
        most_freq_baseline.append("NOT")

    #### EVALUATION ###

    # MOST FREQUENT BASELINE #

    print("MSF: " + '\n')
    print(classification_report(gold_labels, most_freq_baseline))

    # DICTIONARY APPROACH #

    pred_dictionary = []

#    check = ['NOT', 'ABU']

    for elem in set_1:
        id, label = elem
        pred_dictionary.append(label)

    print("Dictionary: " + "\n")
    print(classification_report(gold_labels, pred_dictionary))
    print(confusion_matrix(gold_labels, pred_dictionary))


if __name__ == '__main__':

    abuse_test = "../dalc_v1_test.csv"
    list_offensive = "groflex.tsv" # GROFLEX Lexicon - stored in the GROF_LEX folder

    read_and_match(abuse_test,list_offensive)