from random import randint as rnd
from random import shuffle

def mutation(population_list, n, ps, mr):
    choosen_once = list(range(ps, ps*2))
    shuffle(choosen_once)
    choosen_once = choosen_once[:int(ps*mr)]

    for i in choosen_once:
        cell = rnd(0, n-1)
        val = rnd(0, n-1)
        population_list[i][cell] = val
    return population_list