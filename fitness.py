def fitness(population_list, n):
    lenght = len(population_list)
    for i in range(lenght):
        conflict = 0
        for j in range(n):
            for k in range(j+1, n):
                # Column Conflicts
                if population_list[i][j] == population_list[i][k]:
                    conflict += 1
                # Diagonal Conflicts
                if abs(j-k) == abs(population_list[i][j] - population_list[i][k]):
                    conflict += 1
        population_list[i][-1] = conflict
    return population_list