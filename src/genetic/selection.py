import random
from genetic.population import Population

def roulette_selection(population: Population):
	total_fitness = sum(population.fitness_list)
	limit = random.uniform(0, total_fitness)
	accumulated = 0

	for i in range(len(population.individuals)):
		accumulated += population.fitness_list[i]
		if accumulated >= limit:
			return population.individuals[i], population.fitness_list[i]