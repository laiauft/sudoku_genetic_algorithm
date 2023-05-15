from algorithms.genetic_algorithm import *
import problem.sudoku_structure as sudoku_structure
import sys

args = sys.argv
pop_size = 100

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
        population = crossing_individuals(population, pop_size)

    elif option == 9:
      if len(population) == 0: 
        print("You must generate initial population first.")
      else: population = mutate_individuals(population, puzzle)

    elif option == 0:
      print("Exiting.")
      break
    
if __name__ == '__main__':
    main()
