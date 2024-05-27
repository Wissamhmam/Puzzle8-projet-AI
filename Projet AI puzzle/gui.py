import tkinter as tk
from puzzle import Puzzle8
from algorithms import Algorithms

class Puzzle8GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Puzzle Game")
        self.puzzle = Puzzle8()
        self.algorithms = Algorithms(self.puzzle.goal_state)
        self.create_widgets()
        self.display_puzzle(self.puzzle.init_state)

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()

        self.shuffle_btn = tk.Button(self.root, text="Shuffle", command=self.shuffle)
        self.shuffle_btn.pack(side=tk.LEFT)

        self.solve_hc_btn = tk.Button(self.root, text="Solve Hill Climbing", command=self.solve_hill_climbing)
        self.solve_hc_btn.pack(side=tk.LEFT)

        self.solve_astar_btn = tk.Button(self.root, text="Solve A*", command=self.solve_astar)
        self.solve_astar_btn.pack(side=tk.LEFT)

        self.manual_frame = tk.Frame(self.root)
        self.manual_frame.pack(side=tk.LEFT)

        self.up_btn = tk.Button(self.manual_frame, text="Up", command=lambda: self.manual_move('up'))
        self.up_btn.grid(row=0, column=1)

        self.left_btn = tk.Button(self.manual_frame, text="Left", command=lambda: self.manual_move('left'))
        self.left_btn.grid(row=1, column=0)

        self.right_btn = tk.Button(self.manual_frame, text="Right", command=lambda: self.manual_move('right'))
        self.right_btn.grid(row=1, column=2)

        self.down_btn = tk.Button(self.manual_frame, text="Down", command=lambda: self.manual_move('down'))
        self.down_btn.grid(row=2, column=1)

    def display_puzzle(self, state):
        self.canvas.delete("all")
        for i in range(3):
            for j in range(3):
                num = state[i][j]
                x0, y0 = j * 100, i * 100
                x1, y1 = x0 + 100, y0 + 100
                self.canvas.create_rectangle(x0, y0, x1, y1)
                if num != 0:
                    self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=str(num), font=('Helvetica', 24))

    def shuffle(self):
        self.puzzle.init_state = self.puzzle.generate_puzzle()
        self.display_puzzle(self.puzzle.init_state)

    def manual_move(self, direction):
        self.puzzle.init_state = self.puzzle.manual_move(self.puzzle.init_state, direction)
        self.display_puzzle(self.puzzle.init_state)

    def solve_hill_climbing(self):
        final_state, iterations, moves = self.algorithms.hill_climbing(self.puzzle.init_state, self.puzzle.find_zero)
        self.display_puzzle(final_state)
        print("Initial State:", self.puzzle.init_state)
        print("Final State:", final_state)
        print("Total Iterations:", iterations)
        print("Moves:", moves)

    def solve_astar(self):
        final_state, iterations, moves = self.algorithms.astar(self.puzzle.init_state, self.puzzle.find_zero)
        self.display_puzzle(final_state)
        print("Initial State:", self.puzzle.init_state)
        print("Final State:", final_state)
        print("Total Iterations:", iterations)
        print("Moves:", moves)

if __name__ == "__main__":
    root = tk.Tk()
    app = Puzzle8GUI(root)
    root.mainloop()
