import numpy as np
import pandas as pd
import csv


def ratmat(m, n, fn):
    r = np.zeros((n, m))
    with open(fn, newline='') as csvf:
        csvr = csv.DictReader(csvf)
        for row in csvr:
            mid = int(row['movieId']) - 1
            if mid <= m:
                uid = int(row['userId']) - 1
                r[uid, mid] = float(row['rating'])
    return r


def read_movies(fn):
    df = pd.read_csv(fn)
    return df.loc[df['movieId'] < 10000]


def norm(x, axis=None):
    return np.nan_to_num(x/np.linalg.norm(x, axis=axis))


def map_to_titles(indices, titles):
    return [(indices[i, 0],
             titles.loc[titles['movieId'] == i+1]['title'].item())
            for i in range(indices.shape[0]) if
            titles['movieId'].isin([i+1]).any()]


def movie_profile(x, y, movies_titles):
    z = np.dot(x, norm(y))
    z = norm(z)
    res = np.dot(x.T, z)
    return map_to_titles(res, movies_titles)


def generate_my_rating():
    y = np.zeros((9018, 1))
    y[2570] = 5
    y[31] = 4
    y[259] = 5
    y[1096] = 4
    return y


def main():
    np.seterr(divide='ignore', invalid='ignore')
    fn_r = '../ml-latest-small/ratings.csv'
    fn_m = '../ml-latest-small/movies.csv'
    data = ratmat(9018, 610,  fn_r)
    movies = read_movies(fn_m)
    data = norm(data, axis=0)
    y = generate_my_rating()
    recommended = movie_profile(data, y, movies)
    recommended = sorted(recommended, key=lambda x: x[0], reverse=True)
    names = [y for _, y in recommended]
    print(names)


if __name__ == '__main__':
    main()
