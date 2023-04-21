import numpy as np

def transformar_string_array_de_arrays(sudoku_string):
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

def categorizar_colunas():
  puzzle_array = transformar_string_array_de_arrays("4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......")
  colunas = [[], [], [], [], [], [], [], [], []]

  for i in range(len(puzzle_array)):
      for j in range(len(puzzle_array[i])):
          colunas[j].append(puzzle_array[i][j])
          
  return colunas   
  
def categorize_quadrants(pz):
    pz = np.array(pz).reshape(9, 9)
    quadrants = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            quadrant = pz[i:i+3, j:j+3].flatten().tolist()
            quadrants.append(quadrant)
    return quadrants

def print_linhas_colunas_quadrantes(puzzle_array):
  for i in range(9):
    print(f"Linha {i}: {puzzle_array[i]}")

  print("")
  colunas = categorizar_colunas()
  for i in range(9):
    print(f"Coluna {i}: {colunas[i]}")
    
  print("")
  quadrantes = categorize_quadrants(puzzle_array)
  for i in range(9):
    print(f"Quadrante {i}: {quadrantes[i]}")

puzzle_array = transformar_string_array_de_arrays("4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......")
print_linhas_colunas_quadrantes(puzzle_array)
# print(puzzle_array)