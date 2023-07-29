import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import time

from GeneticAlgorithm import GeneticAlgorithmSolver
from RRHillClimb import BestFirstHillClimbingSolver
from Backtrack import BackTrackSolver

def solution(board):
    lst = len(board) * [0]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                lst[j] = i + 1
    return lst 


def report(algo):
    lst = []
    for i in range(4,15):
        st = time.time()
        board, iters = algo(i)
        end = time.time()
        timing = round((end - st) * 1000.0, 6) #ms
        lst.append((i, iters, solution(board), timing))
    return lst

# backtrack_solver = BackTrackSolver()
# backtrack_data = report(backtrack_solver)
# print(backtrack_data)

# genetic_solver = GeneticAlgorithmSolver()
# genetic_data = report(genetic_solver)
# print(genetic_data)

# RRHC_solver = BestFirstHillClimbingSolver()
# RRHC_data = report(RRHC_solver)
# print(RRHC_data)

def draw_chessboard(board, text):
    N = len(board)

    colors = ['#8B4513', '#F5DEB3']  
    queen_color = 'white'

    plt.figure(figsize=(N, N))
# TODO FIX the position of text
    plt.text(x=0, y=N + 0.1, s=text, fontsize=N * 1.5)
    for i in range(N):
        for j in range(N):
            color = colors[(i + j) % 2]
            plt.gca().add_patch(plt.Rectangle((i, j), 1, 1, color=color))

            if board[i][j] == 1:
                plt.text(i + 0.5, j + 0.5, 'Q', ha='center', va='center', color=queen_color, fontsize=25)

    plt.xticks([])
    plt.yticks([])
    plt.grid(True, color='black', linewidth=1)
    plt.axis('scaled')
    plt.show()

solver_options = ["Select", "BackTrack", "RandomRestartHillClimbing", "GeneticAlgorithm"]

# Create the main application window
root = tk.Tk()
root.title("Dialog Bar")
root.geometry('300x150')

entry_integer_var = tk.StringVar(root)
# Create an entry for the integer
label_integer = tk.Label(root, text="Enter an integer:")
label_integer.pack()
entry_integer = tk.Entry(root, textvariable=entry_integer_var)
entry_integer.pack()

# Create a dropdown for the selective option
label_option = tk.Label(root, text="Select an option:")
label_option.pack()
options = solver_options
option_var = tk.StringVar(root)
option_var.set(options[0])
option_menu = ttk.OptionMenu(root, option_var, *options)
option_menu.pack()


def submit():
    N = int(entry_integer.get())
    solver_name = option_var.get()
    if N <= 3:
        messagebox.showinfo("No solution", f"No available solution for given N : `{N}`")
        raise ValueError(f"No available solution for given N : `{N}`")

    solvers = {
        "BackTrack": BackTrackSolver,
        "RandomRestartHillClimbing": BestFirstHillClimbingSolver,
        "GeneticAlgorithm": GeneticAlgorithmSolver
    }

    solver = solvers.get(solver_name)
    if not solver:
        messagebox.showinfo("Invalid solver", f"Invalid solver selected: `{solver_name}`")
        raise ValueError(f"Invalid solver selected: `{solver_name}`")

    st = time.time()
    board, iters = solver()(N)
    end = time.time()
    timing = round((end - st) * 1000.0, 6)
    text = f"Found solution in {timing}ms within {iters} iterations"
    draw_chessboard(board, text)
  
# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()
# Start the main event loop
root.mainloop()         

N = int(entry_integer_var.get())
if N <= 3:
   messagebox.showinfo("No solution", f"No available solution for given N : `{N}`")
   raise ValueError(f"No available solution for given N : `{N}`")
   
solver_selected = option_var.get()

solvers = {"BackTrack" : BackTrackSolver,
       "RandomRestartHillClimbing" : BestFirstHillClimbingSolver,
       "GeneticAlgorithm" : GeneticAlgorithmSolver}
st = time.time()
board, iters = solvers[solver_selected]()(N)
end = time.time()
timing = round((end - st) * 1000.0, 6)
text = f"Found solution in {timing}ms within {iters} iterations"











