import sys
import sudoku
import numpy as np
from genetic.population import *
from genetic.mutation import mutate_individuals
from genetic.crossing_pairs import crossing_individuals

args = sys.argv
pop_size = 100

def main():
    with open(args[1], 'r') as arq:
        puzzle_string = arq.read()

    puzzle = sudoku.string_to_array(puzzle_string)
    print("Selected puzzle:", puzzle_string)
    print("Population size:", pop_size)
    print("Starting genetic algorithm...")
    print(".\n.\n.")


    ## Step 1: Generate initial random population
    population = Population(puzzle, pop_size)
    print("Generated initial population...")

    ## Step 2: Calculate fitness of individuals
    fitness = population.calculate()
    print("Initial population's fitness calculated...")

    fitness_average = np.mean(fitness)
    fitness_highest = np.max(fitness)
    fitness_lowest = np.min(fitness)
    median_fitness = np.median(fitness)
    print("Average of initial population's fitness:", fitness_average)
    print("Highest initial population's fitness:", fitness_highest)
    print("Lowest initial population's fitness:", fitness_lowest)
    print("Median of  initial population's fitness:", median_fitness)

    criteria = True

    while(criteria):

        parent1 = roulette_selection(population)
        parent2 = roulette_selection(population)

        crossing_individuals(population)

        mutate_individuals(population, puzzle)
    
if __name__ == '__main__':
    main()
