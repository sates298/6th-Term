#!/bin/python
import os
import sys
import re


def counter(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = [ln for ln in f]
        words = [len(re.sub(r'[,\.;\(\)?:\[\]]', ' ', x).split())
                 for x in lines]
    return sum(words), len(lines), max([len(line) for line in lines])


def print_info(bytes, words, lines, max_line):
    print('number of bytes: ', bytes)
    print('number of words: ', words)
    print('number of lines: ', lines)
    print('the longest line: ', max_line)


def main():
    filename = sys.argv[1]
    try:
        print_info(
            os.path.getsize(filename),
            *counter(filename)
        )
    except OSError:
        print('Error with file')


if __name__ == "__main__":
    main()
