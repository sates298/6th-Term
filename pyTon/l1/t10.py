import numpy as np
import matplotlib.pyplot as plt
from math import *

data_size = [80, 24]


def generate_plot(f, a, b):

    def generate_data(f, a, b):
        xs = np.linspace(a, b, num=data_size[0])
        ys = list(map(f, xs))
        round_values = np.linspace(min(ys), max(ys), num=data_size[1])
        rounded = [round_values[np.argmin(
            np.absolute(round_values - x))] for x in ys]
        data = np.vstack((xs, rounded)).conj().transpose()
        return data, round_values

    def print_plot(data, round_values):
        xs = data[:, 0]
        ys = data[:, 1]
        plot = []
        for r in round_values:
            idxs = (ys == r).nonzero()[0].tolist()
            if len(idxs) > 0:
                idxs = list(zip([0]+idxs[:-1], idxs))
                str_ = ' ' if idxs[0] != (0, 0) else '*'
                str_ += '*'.join([''+' '*(x[1] - x[0] - 1)
                                for x in idxs if x[0] != x[1]]) + '*'
                str_ += ' '*(data_size[0] - len(str_))
            else:
                str_ = ' '*data_size[0]
            plot.append(str_)

        if ys.min(0)*ys.max(0) <= 0:
            x_axis = (round_values == round_values[np.argmin(
                np.absolute(round_values - 0))]).nonzero()[0][0]
            plot[x_axis] = '-'*data_size[0]
        if xs.min(0)*xs.max(0) <= 0:
            y_axis = (xs == xs[np.argmin(np.absolute(xs - 0))]).nonzero()[0][0]
            for i in range(len(plot)):
                s = plot[i]
                s = list(s)
                s[y_axis] = '|'
                if s[0] == '-' or s[-1] == '-':
                    s[y_axis] = '+'
                plot[i] = ''.join(s)

        for l in plot[-1::-1]:
            print(l)

    data, rounds = generate_data(f, a, b)
    print_plot(data, rounds)
    return data, rounds


def get_data():
    f = eval('lambda x:' + input('Enter function f: '))
    a = eval(input('Enter start of the range: '))
    b = eval(input('Enter end of the range: '))
    return f, a, b


data, round_ = generate_plot(*get_data())

# plt.ylim(data[:, 1].min(0), data[:, 1].max(0))
# plt.xlim(data[0][0], data[0][-1])
plt.scatter(data[:, 0], data[:, 1])
plt.show()
