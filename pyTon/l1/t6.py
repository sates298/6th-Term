import random as rand

rand.seed()
list_ = [rand.randint(1, 100) for _ in range(20)]

mean_, max_, min_ = sum(list_)/len(list_), max(list_), min(list_)

print('list: ', list_)
print('mean: ', mean_)
print('max: ', max_)
print('min: ', min_)
snd_max, snd_min = max([x for x in list_ if x < max_]), min(
    [x for x in list_ if x > min_])
print('second max: ', snd_max)
print('second min: ', snd_min)
evens = len([x for x in list_ if x % 2 == 0])
print('evens: ', evens)
