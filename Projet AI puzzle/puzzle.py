import random

class Puzzle8:
    def __init__(self):
        self.grid_size = 3
        self.init_state = self.generate_puzzle()
        self.goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def generate_puzzle(self):
        puzzle = list(range(9))
        random.shuffle(puzzle)
        return [puzzle[i:i + 3] for i in range(0, 9, 3)]

    def find_zero(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def manual_move(self, state, direction):
        x, y = self.find_zero(state)
        if direction == 'up' and x > 0:
            state[x][y], state[x-1][y] = state[x-1][y], state[x][y]
        elif direction == 'down' and x < 2:
            state[x][y], state[x+1][y] = state[x+1][y], state[x][y]
        elif direction == 'left' and y > 0:
            state[x][y], state[x][y-1] = state[x][y-1], state[x][y]
        elif direction == 'right' and y < 2:
            state[x][y], state[x][y+1] = state[x][y+1], state[x][y]
        return state
