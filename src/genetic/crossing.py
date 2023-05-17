import math

from genetic.population import Population

def crossing_individuals(population: Population):
	children_population = [] 

	children_count = int(population.size/2)
	for i in range(children_count):

		parents = [population.individuals[i], population.individuals[i+1]]

		c = math.ceil(len(parents[0])/2)
		genes = parents[0][:c] + parents[1][c:]

		children_population.append(genes)
		i = i + 1

	for i in range(len(children_population)):
		print(f'Child {i}: {children_population[i]}')
	
	m = children_count # m = numero de indivíduos antigos mantidos
	new_population = population.individuals[:m] + children_population

	population.individuals = new_population