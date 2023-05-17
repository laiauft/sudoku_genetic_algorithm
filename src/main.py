import sys
import sudoku
import numpy as np
from genetic.population import *
from genetic.mutation import mutate_individuals
from genetic.crossing import crossing_individuals

args = sys.argv
pop_size = 100
mut_tax = 2

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
    fitness = population.calculate()

    print("\t[Initial population]")
    fitness_average = np.mean(fitness)
    fitness_highest = np.max(fitness)
    fitness_lowest = np.min(fitness)
    median_fitness = np.median(fitness)
    print("AVERAGE:\t",fitness_average)
    print("MAX VALUE:\t",fitness_highest)
    print("MIN VALUE:\t",fitness_lowest)
    print("MEDIAN: \t",median_fitness)

    # parent1 = roulette_selection(population)
    # parent2 = roulette_selection(population)

    # print("Parent 1:", parent1)
    # print("Parent 2:", parent2)

    menu_state = True

    while(menu_state):
        print(20*"--")
        print("Choose the options below: ")
        print("1. Display population individuals.")
        print("2. Generate children population.")
        print("3. Mutate individuals in population.")
        print("0. Quit the program.")
        print(20*"--")
        
        option = int(input("--> Option: "))
        print("\n\n")

        if option == 1:
            if len(population.individuals) == 0:
                print("You must generate initial population first.")
            else: 
                for i in range(pop_size):
                    print(f"Individual {i}: {population.individuals[i]}")

        elif option == 2:
            if len(population.individuals) == 0: 
                print("You must generate initial population first.")
            else: 
                crossing_individuals(population)

        elif option == 3:
            if len(population.individuals) == 0: 
                print("You must generate initial population first.")
            else: 
                mutate_individuals(population, puzzle)

        elif option == 0:
            print("Exiting.")
            break
    
if __name__ == '__main__':
    main()