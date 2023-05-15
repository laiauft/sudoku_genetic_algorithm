import math

from genetic.population import Population

def crossing_individuals(population: Population):
	children_population = [] 

	children_count = int(population.size/2)
	for i in range(children_count):
		### OBSERVAÇÃO
		#   por enquanto o pai2 de uma criança será 
		# o pai1 da proxima por conta do contador
		parents = [population.individuals[i], population.individuals[i+1]]

		# Cromossomo = lista de LINHA DO SUDOKU [[]]
		# Gene = linha de VALORES DO SUDOKU     []
		#   A mutação irá envolver alterar o genes 
		# para que seja gerado um novo cromossomo 
		# para um novo individuo da população
		## CRUZAMENTO
		### mutação com um ponto de cruzamento
		# c = crossing_point (PONTO DE CRUZAMENTO)
		c = math.ceil(len(parents[0])/2)
		genes = parents[0][:c] + parents[1][c:]

		children_population.append(genes)
		i = i + 1

	for i in range(len(children_population)):
		print(f'Child {i}: {children_population[i]}')
	
	m = children_count # m = numero de indivíduos antigos mantidos
	new_population = population.individuals[:m] + children_population
	#   A nova população é gerada pelo m indivíduos mantidos 
	# concatenada com a lista de crianças geradas com o tamanho
	# definido como `children_count = int(pop_size/2)`. 
	population.individuals = new_population