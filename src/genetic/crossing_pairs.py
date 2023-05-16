import math

from genetic.population import Population

def crossing_individuals(population: Population):
	children_population = [] 

	children_count = int(population.size/2)
	for i in range(children_count):

		parents = [population.individuals[i], population.individuals[i+1]]

		cutoff = math.ceil(len(parents[0])/2)
		genes = parents[0][:cutoff] + parents[1][cutoff:]

		children_population.append(genes)
		i = i + 1
	
	m = children_count
	new_population = population.individuals[:m] + children_population

	population.individuals = new_population