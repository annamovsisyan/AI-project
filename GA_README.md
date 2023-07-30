# AI-project
Genetic Algorithm
The purpose of the class Chromosome is to store the chessboard states (the locations of the N queens on the N*N board).
Functions:
Generate_random_chromosome: takes an integer and generates a random chromosome of the corresponding size.
Get_random_int: generates a random integer
Get_point: helper function for crossover
Find_chromosome: helper function, returns the index of found val within chroms. -1 otherwise
Chromosome_to_one_hot: takes a list as an input, and returns a nested list representing the locations of queens by 1s and 0s.
GeneticAlgorithmSolver: class to solve the problem by genetic algorithm
mutation: takes a chromosome and, with some probability, swaps two of its queens
crossover: takes two Chromosomes and generates two successor children for the new population's chromosomes
count_fitness: takes a Chromosome and calculates its Fitness(the number of threatening queens).
solve: solves the problem by forming a population, determining the fitness of each one, sorting the given population, and calling crossover and mutation processes. 
main: start point