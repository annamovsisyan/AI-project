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

Backtracking Algorithm


This program uses a backtracking algorithm to find a solution to the N-Queens problem. Backtracking is a systematic way of searching for solutions by trying out different options and undoing them if they lead to a dead-end. The algorithm places queens column by column and backtracks if it finds that the placement violates the rules of the N-Queens problem.

printSolution(board): This utility function takes the solved chessboard configuration and prints it in a human-readable format, displaying the positions of queens as '1' and empty squares as '0'.

solveNQUtil(board, col): This is the recursive utility function that implements the backtracking algorithm. It tries to place a queen in each row of the current column (specified by col). It checks if the queen placement is valid by ensuring it does not attack other queens on the same row, column, or diagonals. If a valid placement is found, the function proceeds to the next column recursively. If a solution is not possible, it backtracks to the previous column and explores other possibilities.

solveNQ(): The main solver function that initializes the chessboard, calls the solveNQUtil function and prints the solution if found. If a solution does not exist, it displays a message stating that no solution was found.

Random Restart Hill Climbing Algorithm


Here we used Random Restart Hill Climbing. It continually explores the solution space and if it fails to find a solution, starts the same from the beginning with a randomly generated combination of queens. This is done continually, until the solution is found.

row_collisions: row_collisions function goes through the chessboard and as a result gives the number of row collisions (number of queens attacking each other in each row)

col_collisions: Like the previous function, col_collisions gives the number of column collisions

evaluate: Calculating total number of collisions based on col_collisions and row_collisions

generate_candidates: This function is given the current state and return all candidate states that are possible arrangements from the current one.

generate_state: generate_state creates random new state (arrangements of queens) for n size n-queens problem.

is_solution: The function checks whether our state is a solution or not with the help of an evaluation function. When evaluation function’s result = 0, that means that there are no queens attacking each other, hence we reached a solution

n_queens_best_first_hill_climbing: This function uses all the above functions and solves the n_queens problem. With the help of hill climbing it tries to find an optimal solution by reducing the number of collisions on the chessboard.

solve_n_queens: solve_n_queens function uses Random Restart Hill Climbing and returns the counted number of random restarts and our final solution.



Main program


There is a report function that takes the algorithms and returns the data for iterations, sample size, solutions and timing for n from 4 to 14.

To run the code one needs to use Python3. 
Initially a small interface will be shown, the one needs to insert an integer value for N (number of queens and size of the chessboard), then choose the algorithm (from three possible options: Genetic, Backtracking and Random Restart Hill-Climbing algorithms) with which one prefers to solve the problem and press submit. The program will print the first valid configuration for the N-Queens problem on the N×N chessboard. If no solution exists, it will display a message indicating the same.




