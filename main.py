from parameters import *
from initial_population import init_population
from cross_over import cross_over
from mutation import mutation
from fitness import fitness
from peresentation import show


current_population = init_population(N, PS)
current_population = fitness(current_population, N)
current_population = sorted(current_population, key=lambda x:x[-1])
if current_population[0][-1] == 0:
        print(f"Solution is found in initial state : {current_population[0]}")
        show(current_population[0], N)
else:
    for i in range(EPOCH):
        current_population = cross_over(current_population, N, PS)
        current_population = mutation(current_population, N, PS, MR)
        current_population = fitness(current_population, N)
        current_population = sorted(current_population, key=lambda x:x[-1])
        current_population = current_population[:PS]
        if current_population[0][-1] == 0:
            print(f"Gneration : {i+1} / Solution Found : {current_population[0]}")
            show(current_population[0], N)
            break
        else:
            print(f"Gneration : {i+1} / Best solution that we found is : {current_population[0]}")
    else:
        print("Sorry, we could not found you a solution")