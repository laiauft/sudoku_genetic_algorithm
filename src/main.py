import sys
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

    menu_state = True

    while(menu_state):
        print(20*"--")
        print("Choose the options below: ")
        print("1. Display population individuals.")
        print("2. Generate new initial population.")
        print("3. Execute program (run generations).")
        print("0. Quit the program.")
        print(20*"--")
        
        option = int(input("--> Option: "))
        print("\n\n")

        if option == 1: # Display Population Individuals
            if len(population.individuals) == 0:
                print("You must generate initial population first.")
            else: 
                for i in range(pop_size):
                    individual = population.individuals[i]
                    print(f"\n\nIndividual {i} - fitness[{individual.fitness}]")
                    for row in population.individuals[i].cromossomo:
                        print(f"{row}")

        elif option == 2: # Generate new initial population
            population = Population(puzzle, pop_size)

        elif option == 3: # Mutate Individuals in Population
            if(population.individuals == 0):
                print("You must generate initial population first.")
            else:
                for i in range(generations):
                    print(f"Gerenation {i}")
                    show_population_stats(population)

                    crossing_one_point(population, int(pop_size/2))
                    mutate_individuals(population, mut_tax)
                    print("\n\n")

        elif option == 0:
            print("Exiting.")
            break
    
if __name__ == '__main__':
    main()