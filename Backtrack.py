import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, messagebox
import time



def draw_chessboard(board):
    N = len(board)

   
    colors = ['#8B4513', '#F5DEB3']  
    queen_color = 'white'

    plt.figure(figsize=(N, N))
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



ld = [0] * 100

rd = [0] * 100

cl = [0] * 100
 
def printSolution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q",end=" ")
            else:
                print(".",end=" ")
        print()
 
class BackTrackSolver:
    def __init__(self):
        self.iterations = 0

    def solve(self, board, col, ld, rd, cl):
        self.iterations += 1
       
        if col >= len(board):
            return True

        for i in range(len(board)):
            if (ld[i - col + len(board) - 1] != 1 and
                rd[i + col] != 1 and cl[i] != 1):

                board[i][col] = 1
                ld[i - col + len(board) - 1] = rd[i + col] = cl[i] = 1

                if self.solve(board, col + 1, ld, rd, cl):
                    return True

                board[i][col] = 0
                ld[i - col + len(board) - 1] = rd[i + col] = cl[i] = 0
       
        return False

    def __call__(self, N):
        self.iterations = 0  # Reset iterations counter
        board = [[0 for _ in range(N)] for _ in range(N)]
        ld = [0] * (2 * N - 1)
        rd = [0] * (2 * N - 1)
        cl = [0] * N

        if not self.solve(board, 0, ld, rd, cl):
            return None  # Return None if no solution is found
        else:
            return board, self.iterations


if __name__ == '__main__':
    #root = tk.Tk()
    #root.withdraw()  

    #visualize_n_queens()
    solver = BackTrackSolver()
    print(solver(8))
 


