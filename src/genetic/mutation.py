import random 

def mutate_individuals(population, puzzle): 

	mutation_tax = 2 

	mutated_individuals = population.individuals[-mutation_tax:] 
	for i in range(len(mutated_individuals)):
		individual = []
		for row in puzzle:
			new_row = []
			for val in row:
				if val == 0: 
					new_row.append(random.randint(1, 9))
				else:
					new_row.append(val)
			individual.append(new_row)
			mutated_individuals[i] = individual
		
	new_population =  population.individuals[:-2] + mutated_individuals
	return new_population 