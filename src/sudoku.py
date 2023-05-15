import numpy as np

def string_to_array(sudoku_string):
  sudoku_list = [sudoku_string[i:i+9] for i in range(0, 81, 9)]

  sudoku_array = []
  for row in sudoku_list:
      row_array = []
      for char in row:
          if char == ".":
              row_array.append(0)
          else:
              row_array.append(int(char))
      sudoku_array.append(row_array)
      
  return sudoku_array

def categorize_columns(puzzle_array):
  columns = [[], [], [], [], [], [], [], [], []]

  for i in range(len(puzzle_array)):
      for j in range(len(puzzle_array[i])):
          columns[j].append(puzzle_array[i][j])
          
  return columns   
  
def categorize_quadrants(pz):
  pz = np.array(pz).reshape(9, 9)
  quadrants = []
  for i in range(0, 9, 3):
      for j in range(0, 9, 3):
          quadrant = pz[i:i+3, j:j+3].flatten().tolist()
          quadrants.append(quadrant)
  return quadrants

def print_rows(puzzle_array):
  for i in range(9):
    print(f"Row {i}: {puzzle_array[i]}")
    
def print_columns(puzzle_array):
  columns = categorize_columns(puzzle_array)
  for i in range(9):
    print(f"Column {i}: {columns[i]}")
    
def print_quadrants(puzzle_array):
  quadrants = categorize_quadrants(puzzle_array)
  for i in range(9):
    print(f"Quadrant {i}: {quadrants[i]}")