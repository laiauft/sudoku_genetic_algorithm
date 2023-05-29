import math
from genetic.individual import Individual
from genetic.population import Population
from genetic.selection import selection_roullete

def crossing_one_point(population: Population, children_count: int):
	children_population = [] 
	# create new 2 individual for each pair of parents 
	for i in range(children_count):
		# select parents from selection method
		parent2 = parent1 = selection_roullete(population)
		while(parent2 == parent1): # two parents should be distinct
			parent2 = selection_roullete(population)
			
		c = math.ceil(len(parent1.cromossomo)/2) # crossing_point

		child1 = Individual(population.puzzle) # first child 
		child1.define_cromossomo(parent1.cromossomo[:c] + parent2.cromossomo[c:]) 

		child2 = Individual(population.puzzle) # second child
		child2.define_cromossomo(parent2.cromossomo[:c] + parent1.cromossomo[c:])

		children_population.extend([child1, child2]); i = i + 1

	# for i in range(len(children_population)):
	# 	print(f'Child {i}:\n{children_population[i].cromossomo}')
	
	m = int(math.ceil(population.size)/2) 
	
	# ord individual by fitness, so best one will be first 
	population.individuals.sort(key=lambda x: x.fitness)
	children_population.sort(key=lambda x: x.fitness)

	# new generation will be half of old population and half new generation
	new_population = population.individuals[:m] + children_population[:m]

	population.new_generation(new_population) # set generation to new one 