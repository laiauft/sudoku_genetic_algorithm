import random
from genetic.individual import Individual

class Population:
	def __init__(self, puzzle, population_size):
		self.puzzle = puzzle
		self.size = population_size
		self.individuals = self.generate()
		self.fitness_list = self.calculate()

	def generate(self):
		population = []

		for _ in range(self.size):
			individual = Individual(self.puzzle)
			population.append(individual)

		return population

	def calculate(self):
		self.fitness_list = []

		num = 216
		for individual in self.individuals:
			total_errors = 0

			for row in individual.cromossomo:
				rows_without_duplicates = set(row)
				errors_in_row = len(row) - len(rows_without_duplicates)
				total_errors += errors_in_row

			columns = zip(*individual.cromossomo)
			for column in columns:
				columns_without_duplicates = set(column)
				errors_in_column = len(column) - len(columns_without_duplicates)
				total_errors += errors_in_column

			for i in range(0, 9, 3):
				for j in range(0, 9, 3):
					quadrant = [row[j:j + 3] for row in individual.cromossomo[i:i + 3]]
					quadrants_without_duplicates = set(row for subgrid in quadrant for row in subgrid)
					errors_in_quadrant = len(quadrant) * 3 - len(quadrants_without_duplicates)
					total_errors += errors_in_quadrant

			fitness = num - total_errors
			self.fitness_list.append(fitness)

		return self.fitness_list
