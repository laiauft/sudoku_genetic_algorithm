import sudoku_structure
import random

pop_size = 2000

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

def rate_fitness_rollet(population, pop_size):
  # Every individual must have a fitness
  # So, an array will storage the value of fitness for every individual
  # The fitness_list[0] is for the first individual: population[0]
  
  fitness_list = [0] * pop_size
  total_errors_list = [0] * pop_size
  num = 216
  
  # Loop that iterates the value of pop_size
  for i in range(pop_size):
    
    for j in range(len(population[i])):
      rowsWithoutDuplicates = [*set(population[i][j])]
      errorsInRow = len(population[i]) - len(rowsWithoutDuplicates)
      total_errors_list[i] += errorsInRow

      population_columns = sudoku_structure.categorize_columns(population[i])
      columnsWithoutDuplicates = [*set(population_columns[j])]
      errorsInColumn = len(population[i]) - len(columnsWithoutDuplicates)
      total_errors_list[i] += errorsInColumn
      
      population_quadrants = sudoku_structure.categorize_quadrants(population[i])
      quadrantsWithoutDuplicates = [*set(population_quadrants[j])]
      errorsInQuadrant = len(population[i]) - len(quadrantsWithoutDuplicates)
      total_errors_list[i] += errorsInQuadrant
      
    fitness_list[i] = num - total_errors_list[i]
      
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
        rate_fitness_rollet(population, pop_size)
    
    elif option == 0:
      print("Exiting.")
      break
    
if __name__ == '__main__':
    main()