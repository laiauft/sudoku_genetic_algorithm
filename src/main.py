import sys
import sudoku
import numpy as np
from genetic.population import *
from genetic.mutation import mutate_individuals
from genetic.crossing_pairs import crossing_individuals

args = sys.argv
pop_size = 100
max_fitness = 216
max_generations = 1000

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
    fitness_median = np.median(fitness)
    print("Average of initial population's fitness:", fitness_average)
    print("Highest initial population's fitness:", fitness_highest)
    print("Lowest initial population's fitness:", fitness_lowest)
    print("Median of  initial population's fitness:", fitness_median)

    criteria = True
    generation = 0

    while criteria and generation < max_generations:
        print("Generation:", generation)

        parent1 = roulette_selection(population)
        parent2 = roulette_selection(population)

        crossing_individuals(parent1, parent2, population)

        population.individuals = mutate_individuals(population, puzzle)

        if max(fitness) == max_fitness:
            print("Solution found!")
            criteria = False
            best_individual = population.individuals[np.argmax(fitness)]

        generation += 1

    if criteria:
        print("Maximum number of generations reached.")
    else:
        print("Best individual:", best_individual)
    
if __name__ == '__main__':
    main()