import requests
import numpy as np
import pandas as pd

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as distance


# nltk.download('vader_lexicon')


def flatten_json(all_data):
    '''
    Just the flatten operation to get what I need
    '''
    users_chats = {}
    for data in all_data:
        users_chats.setdefault(data['user'], []).append(data['text'])

    for k, v in users_chats.items():
        users_chats[k] = ' '.join(v)
    return users_chats


def friend_recomm(all_data):
    '''
    This function, recommend an user as a friend of another, based on the words they mention in their comments 
    '''
    # all_data = all_data.json()
    users_chats = flatten_json(all_data)

    count_vectorizer = CountVectorizer(stop_words='english')
    sparse_matrix = count_vectorizer.fit_transform(users_chats.values())

    doc_term_matrix = sparse_matrix.todense()
    df = pd.DataFrame(doc_term_matrix,
                      columns=count_vectorizer.get_feature_names(),
                      index=users_chats.keys())

    similarity_matrix = distance(df, df)
    sim_df = pd.DataFrame(
        similarity_matrix, columns=users_chats.keys(), index=users_chats.keys())
    np.fill_diagonal(sim_df.values, 0)

    final = sim_df.idxmax()
    friend = {}
    for i, e in final.items():
        friend[i] = e
    print(friend)
    return friend


def side_recomm(all_data):
    '''
    This function tell the user which side of the light they must join,
    based on the positive/neutral/negative words they used in their comments
    '''
    # all_data = all_data.json()
    users_chats = flatten_json(all_data)

    sid = SentimentIntensityAnalyzer()
    users_sentiments = {}
    for user in users_chats:
        users_sentiments[user] = sid.polarity_scores(users_chats[user])

    users_sent = {}
    for keys, values in users_sentiments.items():
        for k, v in values.items():
            if k == 'compound':
                users_sent[keys] = v

    users_join_side = {}
    for k, v in users_sent.items():
        if v > 0:
            users_join_side[k] = 'Light Side'
        elif v < 0:
            users_join_side[k] = 'Dark Side'
        else:
            users_join_side[k] = 'Not defined'
    print(users_join_side)
    return users_join_side
