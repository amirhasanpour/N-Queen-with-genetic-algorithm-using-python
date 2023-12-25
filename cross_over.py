def cross_over(population_list, n, ps):
    for i in range(0, ps, 2):
        childe1 = population_list[i][:n//2] + population_list[i+1][n//2:n] + [None]
        childe2 = population_list[i+1][:n//2] + population_list[i][n//2:n] + [None]
        population_list.append(childe1)
        population_list.append(childe2)
    return population_list