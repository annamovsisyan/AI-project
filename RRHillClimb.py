import random
import matplotlib.pyplot as plt

def row_collisions(a):
    collision = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if j != i:
                collision += 1 if a[i] == a[j] else 0
    return collision

def col_collisions(a):
    collision = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j:
                dp = abs(i - j)
                collision += 1 if a[i] == a[j] + dp or a[i] == a[j] - dp else 0
    return collision // 2

def evaluate(s):
    return col_collisions(s) + row_collisions(s)

def generate_candidates(current):
    candidates = []
    for i in range(len(current)):
        start = current[:i]
        end = current[i + 1:]
        for j in range(1, len(current) + 1):
            c = start + [random.randint(1, len(current))] + end
            candidates.append(c)
    return candidates

def generate_state(n):
    return [random.randint(1, n) for _ in range(n)]

def is_solution(config):
    return evaluate(config) == 0

def n_queens_best_first_hill_climbing(start):
    best = start[:]
    current = start[:]
    current_eval = evaluate(start)

    while True:
        current = best[:]
        candidates = generate_candidates(current)
        for c in candidates:
            candidate_eval = evaluate(c)
            if candidate_eval < current_eval:
                current = c
                current_eval = candidate_eval

        if best == current:
            return best

        best = current[:]

def solve_n_queens(state):
    count = 1
    state = n_queens_best_first_hill_climbing(state)

    while not is_solution(state):
        state = generate_state(len(state))
        count += 1
        state = n_queens_best_first_hill_climbing(state)

    return count, state


def indexes_to_one_hot(indexes):
    board = []
    for i in range(len(indexes)):
        row = [0] * len(indexes)
        row[indexes[i] - 1] = 1
        board.append(row)
    return board

class BestFirstHillClimbingSolver:
    def __init__(self):
        pass
    
    def __call__(self, state):
        count, state = solve_n_queens(generate_state(state))
        board = indexes_to_one_hot(state)
        return board, count

def plot_graphRRHC(x_values, y_values):

    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have the same length.")

    # Create the scatter plot
    plt.plot(x_values, y_values, marker='o', linestyle='-', color='blue', label='Data Points')


    # Add labels and title
    plt.xlabel('Number of Samples')
    plt.ylabel('Number of Restarts')
    plt.title('Plot of SizeOfBoard and Restarts Values')

    # Show the legend
    plt.legend()

    # Display the plot
    plt.show()
    
if __name__ == "__main__":
    solver = BestFirstHillClimbingSolver()
    
    numbers = [i for i in range(4,17)]
    restarts = [state[1] for state in [solver(i) for i in range(4,17)]]
    plot_graphRRHC(numbers, restarts)


