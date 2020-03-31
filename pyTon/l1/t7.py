import random as rand


def check_word(pattern, word):
    for (k, v) in pattern.items():
        if word[k] != v:
            return False
    return True


def find_words(pattern, L):
    if len(pattern) != len(L[0]):
        return []
    patt_dict = {i: pattern[i]
                 for i in range(len(pattern)) if pattern[i] != '*'}
    return list(filter(lambda x: check_word(patt_dict, x), L))


def gen_L(N, one_length, alphabet):
    return [''.join(rand.choices(alphabet, k=one_length)) for _ in range(N)]


rand.seed()
alphabet = ['a', 'b', 'c']
N = 100
length = 8

L = gen_L(N, length, alphabet)
pattern = input('enter pattern: ')

pattern_t = '*a*a*b*c'

print(find_words(pattern, L))
