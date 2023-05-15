import random
import math
import numpy as np

def generate_population(puzzle, pop_size):
    population = []
    puzzle_array = np.array(puzzle)

    for _ in range(pop_size):
        individual = puzzle_array.copy()

        zeros = np.where(individual == 0)
        random_values = np.random.choice(np.arange(1, 10), size=zeros[0].shape, replace=True)

        individual[zeros] = random_values
        population.append(individual.tolist())

    return population

def calculate_fitness(population):
	fitness_list = []

	num = 216
	for individual in population:
		total_errors = 0

		for row in individual:
			rows_without_duplicates = set(row)
			errors_in_row = len(row) - len(rows_without_duplicates)
			total_errors += errors_in_row

		columns = zip(*individual)
		for column in columns:
			columns_without_duplicates = set(column)
			errors_in_column = len(column) - len(columns_without_duplicates)
			total_errors += errors_in_column

		for i in range(0, 9, 3):
			for j in range(0, 9, 3):
				quadrant = [row[j:j + 3] for row in individual[i:i + 3]]
				quadrants_without_duplicates = set(row for subgrid in quadrant for row in subgrid)
				errors_in_quadrant = len(quadrant) * 3 - len(quadrants_without_duplicates)
				total_errors += errors_in_quadrant

		fitness = num - total_errors
		fitness_list.append(fitness)

	return fitness_list

def roulette_selection(population, fitness):
	total_fitness = sum(fitness)
	limit = random.uniform(0, total_fitness)
	accumulated = 0

	for i in range(len(population)):
		accumulated += fitness[i]
		if accumulated >= limit:
			return population[i], fitness[i]