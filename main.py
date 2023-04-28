import sudoku_structure
import random
import numpy

pop_size = 3

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

def rate_fitness(population, pop_size):
  # Every individual must have a fitness
  # So, an array will storage the value of fitness for every individual
  # The fitness_list[0] is for the first individual: population[0]
  
  fitness_list = [0] * pop_size
  
  # Loop that iterates the value of pop_size
  for i in range(pop_size):
    
    print(f"Individual {i} --> {population[i]}")
    
    for j in range(len(population[i])):
      print(f"{j}º row of Individual {i} --> {population[i][j]}")
      withoutDuplicates = [*set(population[i][j])]
      print(f"{j}º row of Individual {i} --> {withoutDuplicates}")
      errorsInRow = len(population[i]) - len(withoutDuplicates)
      print(f"{j}º row of Individual {i} Errors --> {errorsInRow}")
      fitness_list[i] += errorsInRow
      
    print("")
    # res = 
    # print(res)
    
  
  for i in range(len(fitness_list)):
    print(f"Fitness of individual {i} --> {fitness_list[i]}")

    
    

def main():
  print("Insert the puzzle as string: ")
  puzzle_string = input()
  puzzle = sudoku_structure.string_to_array(puzzle_string)
  
  menu_state = True
  
  while(menu_state):
    
    print(20*"--")
    print("Choose the options below: ")
    print("1. Print rows.")
    print("2. Print columns.")
    print("3. Print quadrants.")
    print("4. Use another puzzle.")
    print("5. Generate initial population.")
    print("6. Rate fitness.")
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
      for i in range(pop_size):
        print(f"Individual {i}: {population[i]}")
    
    elif option == 6:
      if len(population) == 0:
        print("You must generate initial population first.")
      else:
        rate_fitness(population, pop_size)
    
    elif option == 0:
      print("Exiting.")
      break
    
if __name__ == '__main__':
    main()