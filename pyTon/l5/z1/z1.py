import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.graph_objs as go


# %%

def read_rating_from_csv(fn):
    df = pd.read_csv(fn)
    users = df.loc[df['movieId'] == 1].reset_index()[['userId']]
    user_indices = {users['userId'][i]: i for i in users.index}
    movies = df[df['userId'].isin(users['userId'])].iloc[:, :3]
    return user_indices, movies


def get_X(fn, m):
    users, movies = read_rating_from_csv(fn)
    data = np.zeros((len(users), m), dtype=np.float64)
    y = np.zeros(len(users))
    for _, row in movies.iterrows():
        mve = row['movieId']
        if mve == 1:
            y[users[row['userId']]] = row['rating']
        elif mve < m+2:
            data[users[row['userId']], int(mve) - 2] = row['rating']
    return data, y
# %%


def get_pred(X_train, Y_train, X_test):
    model = LinearRegression()
    model.fit(X_train, Y_train)
    return model.predict(X_test)


# %%
def print_plot(Y_pred, Y_true, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.linspace(0, Y_true.shape[0], Y_true.shape[0]),
                             y=Y_true,
                             mode='markers',
                             name='test'))
    fig.add_trace(go.Scatter(x=np.linspace(0, Y_pred.shape[0], Y_pred.shape[0]),
                             y=Y_pred,
                             mode='lines',
                             name='pred'))
    fig.update_layout(title=title)
    # fig.show()
    return fig

# %%


def run_first(fn, m, fn_out):
    X, Y = get_X(fn, m)
    Y_pred = get_pred(X, Y, X)
    fig = print_plot(Y_pred, Y, f'm={m}')
    fig.write_html(fn_out)


def run_second(fn, m, fn_out):
    X, Y = get_X(fn, m)
    X_train, Y_train = X[:-15], Y[:-15]
    X_test, Y_test = X[-15:], Y[-15:]
    Y_pred = get_pred(X_train, Y_train, X_test)
    fig = print_plot(Y_pred, Y_test, f'm={m}')
    fig.write_html(fn_out)

# %%


def main():
    mfst = [10, 100, 1000, 10000]
    msnd = [10, 100, 200, 500, 1000, 10000]
    dir_name = '~/Documents/repos/6th-Term/pyTon/l5/'
    fn = dir_name + 'ml-latest-small/ratings.csv'
    for m in mfst:
        fn_out = f'plots/regression_m_{m}.html'
        run_first(fn, m, fn_out)
    for m in msnd:
        fn_out = f'plots/predicate_m_{m}.html'
        run_second(fn, m, fn_out)


if __name__ == '__main__':
    main()
