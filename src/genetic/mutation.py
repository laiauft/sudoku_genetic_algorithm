import math
import random
from genetic.population import Population

def mutate_individuals(population: Population, mutation_tax: float): 
	#   a taxa de mutação infere quantos indivíduos terão seus 
	# genes mutados e não a quantidade de genes mutados no individuo

	# mutated_individuals = population.individuals[-mutation_tax:] 
		
	total_cells = 81 	# total de celulas no sudoku
	numbers_mask = []	# lista de valores reais nas mascara

	for row in population.puzzle:
		new_row = []
		for val in row:
			if val != 0: # se o valor é igual a zero, ele deve 
				# ser atribuido a mascara, pois ele é um valor padrão
				new_row.append(val)
			else: # caso contrário deve ser substituido por None
				new_row.append(None)
		numbers_mask.append(new_row) # a mascara recebe sua nova linha


	mutated_individuals = []
	# ordena os elementos para colocar os piores por ultimo
	population.individuals.sort(key=lambda x: x.fitness, reverse=True)
	# percorre todos os elementos da lista de individuos
	for i in range(len(population.individuals)):
		# apartir do indice menor que a porcentagem da taxa de mutação
		if i <= (population.size * mutation_tax): 	# apenas elementos abaixo 
			# ou igual a taxa de mutação (porcentagem da população) será mutado
			mutated = population.individuals[i] 	# ele ira mutar os individuos
			for k in range(len(mutated.cromossomo)): 
				# percorrendo cada linha dentro do gene do cromomosso	
				individual_row = mutated.cromossomo[k]
				numbers_mask_row = numbers_mask[k] 
				for j in range(len(row)): 
					# compara o valor correspondente da mascara com o valor do gene
					if(individual_row[j] != numbers_mask_row[j]): 
						# se o valor for diferente, portanto não faz parte da mascara
						# ele podera mutar o valor do individuo sem prejudicar o resultado
						if random.randint(1, total_cells) == 1: 
							# agora o individuo passa por outra triagem que define se 
							# o seu valor terá probabilidade de ser mutado de fato ou não
							mutated.cromossomo[k][j] = random.randint(1, 9)
							mutated.calculate_fitness()
							break # uma vez que o valor é mutado ele deve sair dos laços
					else:
						continue
					break
				break
			# contudo os outros individuos devem ter suas chances de serem mutados e por 
			# isso o último laço prevelacerá para que assim todos os membros da população
			# abaixo da taxa (ou igual) a porcentagem de mutação passaram pela mesma triagem
			mutated_individuals.append(mutated)
		population.individuals[i] = mutated
	
	i = 0
	for i in range(len(mutated_individuals)):
		print(f"Mutated Individual [{i}]", end=" - ") 
		print(f"fitness[{mutated_individuals[i].fitness}]")
		for row in mutated_individuals[i].cromossomo:
			print(row)
		print()
	# print(f'Mutated Individual {i}:\n{mutated_individuals[i]}')
