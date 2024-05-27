import copy
import heapq
from collections import deque

class Algorithms:
    def __init__(self, goal_state):
        self.goal_state = goal_state

    def heuristic(self, state):
        return sum(state[i][j] != self.goal_state[i][j] for i in range(3) for j in range(3))

    def get_neighbors(self, state, find_zero):
        neighbors = deque()
        x, y = find_zero(state)
        directions = [('up', -1, 0), ('down', 1, 0), ('left', 0, -1), ('right', 0, 1)]
        for direction, dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                neighbor = copy.deepcopy(state)
                neighbor[x][y], neighbor[nx][ny] = neighbor[nx][ny], neighbor[x][y]
                neighbors.append((neighbor, direction))
        return neighbors

    def hill_climbing(self, state, find_zero):
        moves = []
        iterations = 0
        current_state = copy.deepcopy(state)
        while self.heuristic(current_state) != 0:
            neighbors = self.get_neighbors(current_state, find_zero)
            next_state, direction = min(neighbors, key=lambda x: self.heuristic(x[0]))
            if self.heuristic(next_state) >= self.heuristic(current_state):
                print(f"Stuck at local minima with heuristic {self.heuristic(current_state)}")
                break
            current_state = next_state
            moves.append(direction)
            iterations += 1
        return current_state, iterations, moves

    def astar(self, state, find_zero):
        open_list = []
        heapq.heappush(open_list, (self.heuristic(state), state, []))
        closed_set = set()
        iterations = 0

        while open_list:
            _, current_state, path = heapq.heappop(open_list)
            iterations += 1

            if current_state == self.goal_state:
                return current_state, iterations, path

            closed_set.add(tuple(map(tuple, current_state)))

            for neighbor, direction in self.get_neighbors(current_state, find_zero):
                if tuple(map(tuple, neighbor)) not in closed_set:
                    new_path = path + [direction]
                    heapq.heappush(open_list, (self.heuristic(neighbor) + len(new_path), neighbor, new_path))

        return state, iterations, []
