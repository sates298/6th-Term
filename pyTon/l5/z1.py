import numpy as np
import pandas as pd


def read_rating_from_csv(fn):
    df = pd.read_csv(fn)
    users = df.loc[df['movieId'] == 1].reset_index()[['userId']]
    return users, df[df['userId'].isin(users['userId'])].iloc[:, :3]


dir_name = '~/Documents/repos/6th-Term/pyTon/l5/ml-latest-small/'
fn = dir_name + 'ratings.csv'
users, rating = read_rating_from_csv(fn)
rating
users['userId'][3]
user_indexes = {users['userId'][i]: i for i in users.index}
user_indexes
