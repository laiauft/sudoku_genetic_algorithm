import math
from genetic.individual import Individual
from genetic.population import Population
from genetic.selection import selection_roullete

def crossing_one_point(population: Population, children_count: int):
	children_population = [] 
	for i in range(children_count):
		parent2 = parent1 = selection_roullete(population)
		while(parent2 == parent1):
			parent2 = selection_roullete(population)
			
		# c = crossing_point
		c = math.ceil(len(parent1.cromossomo)/2)
		child1 = Individual(population.puzzle) 
		child2 = Individual(population.puzzle)
		child1.define_cromossomo(parent1.cromossomo[:c] + parent2.cromossomo[c:]) 
		child2.define_cromossomo(parent1.cromossomo[:c] + parent2.cromossomo[c:])

		children_population.append(child1)
		i = i + 1

	for i in range(len(children_population)):
		print(f'Child {i}:\n{children_population[i].cromossomo}')
	
	m = children_count # m = numero de indivíduos antigos mantidos
	new_population = population.individuals[:m] + children_population

	population.individuals = new_population