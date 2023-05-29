import sys
import csv
import sudoku
import numpy as np
from genetic.population import Population
from genetic.mutation import mutate_individuals
from genetic.crossing import crossing_one_point

args = sys.argv
pop_size = 100
mut_tax = 0.05
generations = 100

def show_population_stats(population: Population) -> None:
    fitness_average = np.mean(population.fitness_list)
    fitness_highest = np.max(population.fitness_list)
    fitness_lowest = np.min(population.fitness_list)
    median_fitness = np.median(population.fitness_list)

    print("AVERAGE:\t",fitness_average)
    print("MAX VALUE:\t",fitness_highest)
    print("MIN VALUE:\t",fitness_lowest)
    print("MEDIAN: \t",median_fitness)

def write_generation_info_to_csv(filename: str, generation: int, population: Population) -> None:
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([generation] + population.fitness_list)

def main():
    with open(args[1], 'r') as arq:
        puzzle_string = arq.read()

    puzzle = sudoku.string_to_array(puzzle_string)
    print("Selected puzzle:", puzzle_string)
    print("Population size:", pop_size)
    print("Starting genetic algorithm...")
    print(".\n.\n.")

    population = Population(puzzle, pop_size)
    print("Generated initial population...")

    print("\t[Initial population]")
    show_population_stats(population)

    csv_filename = "generation_info.csv"

    for i in range(generations):
        print(f"Generation {i}")
        show_population_stats(population)

        write_generation_info_to_csv(csv_filename, i, population)

        crossing_one_point(population, int(pop_size/2))
        mutate_individuals(population, mut_tax)
        print("\n\n")

    
if __name__ == '__main__':
    main()