import sudoku_structure
import random
import threading

pop_size = 5

class GenerateIndividualThread(threading.Thread):
  def __init__(self, puzzle, individual_number):
    threading.Thread.__init__(self)
    self.puzzle = puzzle
    self.individual_number = individual_number
    self.individual = None

  def run(self):
    self.individual = []
    for row in self.puzzle:
      new_row = []
      for val in row:
        if val == 0:
          new_row.append(random.randint(1, 9))
        else:
          new_row.append(val)
      self.individual.append(new_row)

  def get_individual(self):
    return self.individual

def generate_population(puzzle, pop_size):
  threads = []
  for i in range(pop_size):
    thread = GenerateIndividualThread(puzzle, i)
    threads.append(thread)
    thread.start()

  population = []
  for thread in threads:
    thread.join()
    population.append(thread.get_individual())

  return population
  

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
    print("0. Quit the program.")
    print(20*"--")
    
    option = int(input("\n\nOption: "))
    
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
    
    elif option == 0:
      print("Exiting.")
      break
    
if __name__ == '__main__':
    main()