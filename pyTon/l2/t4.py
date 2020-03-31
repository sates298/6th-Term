#!/bin/python
import os
import sys
import hashlib


def memorize(f):
    global files
    files = {}

    def inner(deer):
        list = f(deer)
        for (name, hsh, size) in list:
            if (hsh, size) in files:
                files[(hsh, size)].add(name)
            else:
                files[(hsh, size)] = set([name])
        return list
    return inner


@memorize
def check_files(deer):
    list = []
    for f in os.listdir(deer):
        file = os.path.join(deer, f)
        if os.path.isdir(file):
            check_files(file)
        else:
            with open(file, 'rb') as fl:
                size = os.path.getsize(file)
                hash_file = hashlib.sha256(fl.read()).hexdigest()
                list.append((file, hash_file, size))
    return list


def print_files():
    for v in files.values():
        print('================================')
        for f in v:
            print(f)
    print('================================')


if __name__ == "__main__":
    deername = sys.argv[1]
    check_files(deername)
    print_files()
