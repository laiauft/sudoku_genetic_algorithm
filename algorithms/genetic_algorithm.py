import random
import math

def generate_population(puzzle, pop_size):
  population = []
  for _ in range(pop_size):
    individual = []
    for row in puzzle:
      new_row = []
      for val in row:
        if val == 0:
          new_row.append(random.randint(1, 9))
        else:
          new_row.append(val)
      individual.append(new_row)
    population.append(individual)
  return population

def crossing_individuals(population, pop_size):
  children_population = [] 

  children_count = int(pop_size/2)
  for i in range(children_count):
    ### OBSERVAÇÃO
    #   por enquanto o pai2 de uma criança será 
    # o pai1 da proxima por conta do contador
    parents = [population[i], population[i+1]]

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
  new_population = population[:m] + children_population
  #   A nova população é gerada pelo m indivíduos mantidos 
  # concatenada com a lista de crianças geradas com o tamanho
  # definido como `children_count = int(pop_size/2)`. 
  return new_population

def mutate_individuals(population, puzzle): 
  #   a taxa de mutação infere quantos indivíduos terão seus 
  # genes mutados e não a quantidade de genes mutados no individuo
  mutation_tax = 2 

  mutated_individuals = population[-2:] 
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
    print(f'Mutated Individual {i}: {mutated_individuals[i]}')
    i = i + 1
  new_population =  population[:-2] + mutated_individuals
  return new_population 


def calculate_fitness(population):
    fitness_list = []

    num = 216
    for individual in population:
        total_errors = 0

        for row in individual:
            rows_without_duplicates = set(row)
            errors_in_row = len(row) - len(rows_without_duplicates)
            total_errors += errors_in_row

        columns = zip(*individual)
        for column in columns:
            columns_without_duplicates = set(column)
            errors_in_column = len(column) - len(columns_without_duplicates)
            total_errors += errors_in_column

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                quadrant = [row[j:j + 3] for row in individual[i:i + 3]]
                quadrants_without_duplicates = set(row for subgrid in quadrant for row in subgrid)
                errors_in_quadrant = len(quadrant) * 3 - len(quadrants_without_duplicates)
                total_errors += errors_in_quadrant

        fitness = num - total_errors
        fitness_list.append(fitness)

    return fitness_list

def roulette_selection(population, fitness):
    total_fitness = sum(fitness)
    limit = random.uniform(0, total_fitness)
    accumulated = 0

    for i in range(len(population)):
        accumulated += fitness[i]
        if accumulated >= limit:
            return population[i], fitness[i]