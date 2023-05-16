import sys
import sudoku
import numpy as np
from genetic.population import *
from genetic.mutation import mutate_individuals
from genetic.crossing_pairs import crossing_individuals

args = sys.argv
pop_size = 100
<<<<<<< HEAD
max_fitness = 216
max_generations = 1000
=======
>>>>>>> parent of 322ce0b (FEAT new objects created in genetic module)

def main():
    with open(args[1], 'r') as arq:
        puzzle_string = arq.read()

    puzzle = sudoku.string_to_array(puzzle_string)
    print("Selected puzzle:", puzzle_string)
    print("Population size:", pop_size)
    print("Starting genetic algorithm...")
    print(".\n.\n.")

<<<<<<< HEAD

    ## Step 1: Generate initial random population
    population = Population(puzzle, pop_size)
    print("Generated initial population...")

    ## Step 2: Calculate fitness of individuals
    fitness = population.calculate()
=======
    population = generate_population(puzzle, pop_size)
    print("Generated initial population...")
    fitness = calculate_fitness(population)
>>>>>>> parent of 322ce0b (FEAT new objects created in genetic module)
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

<<<<<<< HEAD
    while criteria and generation < max_generations:
        print("Generation:", generation)
=======
    parent1 = roulette_selection(population, fitness)
    parent2 = roulette_selection(population, fitness)
>>>>>>> parent of 322ce0b (FEAT new objects created in genetic module)

        parent1 = roulette_selection(population)
        parent2 = roulette_selection(population)

        crossing_individuals(parent1, parent2, population)

<<<<<<< HEAD
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
=======
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
            if len(population) == 0:
                print("You must generate initial population first.")
            else: 
                for i in range(pop_size):
                    print(f"Individual {i}: {population[i]}")

        elif option == 2:
            if len(population) == 0: 
                print("You must generate initial population first.")
            else: 
                population = crossing_individuals(population, pop_size)

        elif option == 3:
            if len(population) == 0: 
                print("You must generate initial population first.")
            else: 
                population = mutate_individuals(population, puzzle)

        elif option == 0:
            print("Exiting.")
            break
>>>>>>> parent of 322ce0b (FEAT new objects created in genetic module)
    
if __name__ == '__main__':
    main()
