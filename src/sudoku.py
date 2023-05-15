import numpy as np

def string_to_array(sudoku_string):
    sudoku_list = [sudoku_string[i:i+9] for i in range(0, 81, 9)]
    sudoku_array = np.zeros((9, 9), dtype=int)

    for i, row in enumerate(sudoku_list):
        for j, char in enumerate(row):
            if char != ".":
                sudoku_array[i, j] = int(char)

    return sudoku_array


def categorize_columns(puzzle_array):
    columns = np.transpose(puzzle_array).tolist()
    
    return columns
  
def categorize_quadrants(puzzle_array):
    puzzle_array = np.array(puzzle_array).reshape(9, 9)
    quadrants = []

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            quadrant = puzzle_array[i:i+3, j:j+3].flatten().tolist()
            quadrants.append(quadrant)

    return quadrants