from algorithms.genetic_algorithm import calculate_fitness, generate_population, roulette_selection
import problem.sudoku_structure as sudoku_structure
import sys
import math
import random

args = sys.argv
pop_size = 100

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

def crossing_individuals(population):
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

def main():
  print("Starting...")
  with open(args[1], 'r') as arq:
    puzzle_string = arq.read()

  puzzle = sudoku_structure.string_to_array(puzzle_string)
  
  menu_state = True
  
  population = []

  while(menu_state):
    
    print(20*"--")
    print("Choose the options below: ")
    print("1. Print rows.")
    print("2. Print columns.")
    print("3. Print quadrants.")
    print("4. Use another puzzle.")
    print("5. Generate initial population.")
    print("6. Rate fitness.")
    print("7. Display population individuals.")
    print("8. Generate children population.")
    print("9. Mutate individuals in population.")
    print("0. Quit the program.")
    print(20*"--")
    
    option = int(input("--> Option: "))
    print("\n\n")
    
    if option == 1:
      sudoku_structure.print_rows(puzzle)
    
    elif option == 2:
      sudoku_structure.print_columns(puzzle)
    
    elif option == 3:
      sudoku_structure.print_quadrants(puzzle)
      
    elif option == 4:
      print("Insert the puzzle as string: ")
      puzzle_string = input()
      puzzle = sudoku_structure.string_to_array(puzzle_string)
      
    elif option == 5:
      population = generate_population(puzzle, pop_size)
      print("")
      # for i in range(pop_size):
      #   print(f"Individual {i}: {population[i]}")
    
    elif option == 6:
      if len(population) == 0:
        print("You must generate initial population first.")
      else:
        fitness = calculate_fitness(population)
        parent1 = roulette_selection(population, fitness)
        parent2 = roulette_selection(population, fitness)

        print("Parent 1:", parent1)
        print("Parent 2:", parent2)
    
    elif option == 7:
      if len(population) == 0:
        print("You must generate initial population first.")
      else: 
        for i in range(pop_size):
          print(f"Individual {i}: {population[i]}")

    elif option == 8:
      if len(population) == 0: 
        print("You must generate initial population first.")
      else: 
        population = crossing_individuals(population)

    elif option == 9:
      if len(population) == 0: 
        print("You must generate initial population first.")
      else: population = mutate_individuals(population, puzzle)

    elif option == 0:
      print("Exiting.")
      break
    
if __name__ == '__main__':
    main()
