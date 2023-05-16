import math

<<<<<<< HEAD
from genetic.population import Population

def crossing_individuals(parent1, parent2, population: Population):
=======
def crossing_individuals(population, pop_size):
>>>>>>> parent of 322ce0b (FEAT new objects created in genetic module)
	children_population = [] 

	children_count = int(pop_size/2)
	for i in range(children_count):
<<<<<<< HEAD
=======
		### OBSERVAÇÃO
		#   por enquanto o pai2 de uma criança será 
		# o pai1 da proxima por conta do contador
		parents = [population[i], population[i+1]]
>>>>>>> parent of 322ce0b (FEAT new objects created in genetic module)

		cutoff = math.ceil(len(parent1)/2)
		genes = parent1[:cutoff] + parent2[cutoff:]

		children_population.append(genes)
		i = i + 1
	
<<<<<<< HEAD
	m = children_count
	new_population = population.individuals[:m] + children_population

	population.individuals = new_population
=======
	m = children_count # m = numero de indivíduos antigos mantidos
	new_population = population[:m] + children_population
	#   A nova população é gerada pelo m indivíduos mantidos 
	# concatenada com a lista de crianças geradas com o tamanho
	# definido como `children_count = int(pop_size/2)`. 
	return new_population
>>>>>>> parent of 322ce0b (FEAT new objects created in genetic module)
