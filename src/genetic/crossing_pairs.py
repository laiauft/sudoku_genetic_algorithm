import math

from genetic.population import Population

def crossing_individuals(parent1, parent2, population: Population):
	children_population = [] 

	children_count = int(population.size/2)
	for i in range(children_count):

		cutoff = math.ceil(len(parent1)/2)
		genes = parent1[:cutoff] + parent2[cutoff:]

		children_population.append(genes)
		i = i + 1
	
	m = children_count
	new_population = population.individuals[:m] + children_population

	population.individuals = new_population