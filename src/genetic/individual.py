import random

class Individual:
    def __init__(self, puzzle) -> None:
        self.cromossomo = self.generate_cromossomo(puzzle) 
        self.calculate_fitness()

    def generate_cromossomo(self, puzzle) -> list[int]:
        cromossomo = []
        for row in puzzle:
            new_row = []
            for val in row:
                if val == 0:
                    val = random. randint(1, 9)
                new_row.append(val)
            cromossomo.append(new_row)
        return cromossomo

    def define_cromossomo(self, genes) -> None:
        self.cromossomo = genes
        self.calculate_fitness()

    def calculate_fitness(self) -> None:
        num  = 216
        total_erros = 0 
        for row in self.cromossomo:
            rows_without_duplicates = set(row)
            errors_in_row = len(row) - len(rows_without_duplicates)
            total_erros += errors_in_row

        columns = zip(*self.cromossomo)
        for column in columns:
            columns_without_duplicates = set(columns)
            erros_in_column = len(column) - len(columns_without_duplicates)
            total_erros += erros_in_column

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                quadrant = [row[j:j + 3] for row in self.cromossomo[i:i + 3]]
                quadrants_without_duplicates = set(row for subgrid in quadrant for row in subgrid)
                erros_in_quandrant = len(quadrant) * 3 - len(quadrants_without_duplicates)
                total_erros += erros_in_quandrant

        self.fitness = num - total_erros
