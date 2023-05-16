import random 

def mutate_individuals(population, puzzle): 

	mutation_tax = 2 

	mutated_individuals = population[-mutation_tax:] 
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
			print(f"size:{len(mutated_individuals)}")
			mutated_individuals[i] = individual
<<<<<<< HEAD
		
	new_population =  population.individuals[:-2] + mutated_individuals
=======
			print(f'Mutated Individual {i}: {mutated_individuals[i]}')
	new_population =  population[:-2] + mutated_individuals
>>>>>>> parent of 322ce0b (FEAT new objects created in genetic module)
	return new_population 