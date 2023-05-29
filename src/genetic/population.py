import random
from genetic.individual import Individual

class Population:
	def __init__(self, puzzle, population_size):
		self.puzzle = puzzle
		self.size = population_size
		self.individuals = self.generate()
		self.fitness_list = self.calculate()

	def generate(self) -> list[Individual]:
		population = []

		for _ in range(self.size):
			individual = Individual(self.puzzle)
			population.append(individual)

		return population

	def calculate(self) -> list[int]:
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
	
	def sort_individuals_by_fitness(self):
		self.individuals.sort(lambda x: x.fitness, reverse=True)
		#list_sort = sorted([(self.fitness_list[i], self.individuals[i]) for i in range(len(self.individuals))], key=lambda x: x[0], reverse=True)
		#self.individuals[:] = list(map(lambda x: x[1], list_sort))[:]


	def calculate_fitness_pop(self):
		_ = [e.calculate_fitness() for e in self.individuals]
		self.individuals[:] = list(map(lambda x: x.fitness, self.individuals))[:]

		self.sort_individuals_by_fitness()

		for i in range(len(self.individuals)):
			print(f'Individual {i}:\n{self.individuals[i]}')