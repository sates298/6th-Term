#!/bin/python
import os
import sys


def change_files(deer):
    for file in os.listdir(deer):
        f = os.path.join(deer, file)
        low = f.lower()
        os.rename(f, low)
        if os.path.isdir(low):
            change_files(low)


if __name__ == "__main__":
    deername = sys.argv[1]
    change_files(deername)
