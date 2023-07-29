import math
import random
from chromosome import Chromosome
from typing import List, Union

MAX_ITER = 5500
POPULATION_SIZE = 1000

def generate_random_chromosome(size: int) -> Chromosome:
    l = list(range(size))
    random.shuffle(l)
    c = Chromosome(size)
    for i in range(size):
        c.set(i, l[i])
    return c

def get_random_int(min_: int, max_: int) -> int:
    return int(math.floor(random.random() * (max_ - min_ + 1) + min_))

def get_point(val: int, size: int) -> int:
    min_ = 1
    max_ = size - 1
    point = get_random_int(min_, max_)
    if (point == val):
        return get_point(val, size)
    return point

def find_chromosome(val : int, chroms : Chromosome) -> int:
    # returns index of found val within chroms. -1 otherwise
    for i in range(len(chroms)):
        if (chroms.get(i) == val):
            return i
    return -1

def chromosome_to_one_hot(chr : Chromosome) -> List[List[int]]:
    indexes = []
    for i in range(len(chr)):
        indexes.append(chr.get(i))
    board = []
    for i in range(len(indexes)):
        row = [0] * len(indexes)
        row[indexes[i]] = 1
        board.append(row)
    return board


class GeneticAlgorithmSolver:
    
    def __init__(self, max_iter=MAX_ITER):
        self.iterations = 0
        self.max_iter = max_iter


    def mutation(self, ch : Chromosome, prob: float) -> Chromosome:
        max_ = 1
        min_ = 0
        size = len(ch) - 1
        rand_prob = math.floor(random.random() * (max_ - min_ + 1) + min_)

        rand_index1 = 0
        rand_index2 = 0

        if (prob <= rand_prob):
            rand_index1 = get_random_int(min_, size)
            rand_index2 = get_random_int(min_, size)
            if (rand_index1 != rand_index2):
                tmp_val = ch.get(rand_index1)
                ch.set(rand_index1, ch.get(rand_index2))
                ch.set(rand_index2, tmp_val)
        return ch

    def crossover(self, parent1 : Chromosome, parent2 : Chromosome) -> List[Chromosome]:
        length = len(parent1)
        max_ = length - 1
        min_ = 0

        child1 = Chromosome(length)
        child2 = Chromosome(length)

        p1 = get_random_int(min_, max_)
        p2 = get_point(p1, length)

        if (p1 > p2):
            p1, p2 = p2, p1

        for i in range(p1, p2):
            child1.set(i, parent1.get(i))
            child2.set(i, parent2.get(i))

        for i in range(length):
            if (0 == child1.get(i)):
                for j in range(length):
                    if find_chromosome(parent2.get(j), child1) == -1:
                        child1.set(i, parent2.get(j))
                        break

        for i in range(length):
            if (0 == child2.get(i)):
                for j in range(length):
                    if find_chromosome(parent1.get(j), child2) == -1:
                        child2.set(i, parent1.get(j))
                        break
        return [child1, child2]

    def count_fitness(self, ch: Chromosome) -> int:
        rep_queens1, rep_queens2 = 0, 0
        length = len(ch)

        diag1, diag2 = [], []

        for i in range(length):
            diag1.append(ch.get(i) - (i + 1))
            diag2.append(1 + length - ch.get(i) - (i + 1))
        
        diag1.sort()
        diag2.sort()

        for i in range(length):
            if (diag1[i] == diag1[i - 1]):
                rep_queens1 += 1
            if (diag2[i] == diag2[i - 1]):
                rep_queens2 += 1

        return rep_queens1 + rep_queens2

    def solve(self, population: List[Chromosome], mut_prob: float) -> Union[Chromosome,None]:
        if (self.iterations > self.max_iter):
            return None

        self.iterations += 1

        population_fitness = []
        size = len(population)

        for i in range(size):
            fitness = self.count_fitness(population[i])
            population_fitness.append(fitness)
            if (0 == fitness):
                return population[i]

        fitness_to_sort = population_fitness.copy()
        fitness_to_sort.sort()
        
        total_population = []
        for i in range(size):
            for j in range(size):
                if (population_fitness[j] == fitness_to_sort[i]):
                    total_population.append(population[j])
                    population_fitness[j] = -5
                    break

        new_population = []
        for i in range(0, size - 1, 2):
            child1, child2 = self.crossover(total_population[i], total_population[i + 1])
            chr1 = self.mutation(child1, mut_prob)
            chr2 = self.mutation(child2, mut_prob)
            new_population.append(self.mutation(chr1, 0.3))
            new_population.append(self.mutation(chr2, 0.3))

        return self.solve(new_population, mut_prob)

    def __call__(self, n):
        
        if (2 == n) or (3 == n):
            raise ValueError(f"No solution for given `{n}`")
        population = []
        for _ in range(POPULATION_SIZE):
            population.append(generate_random_chromosome(n))
    
        solution = self.solve(population, 0.0)
        if not solution is None:
            solution = chromosome_to_one_hot(solution)
            return solution, self.iterations
        return None

if __name__ == "__main__":
    solver = GeneticAlgorithmSolver()
    print(solver(13))
