
class Node:
    def __init__(self, puzzle, depth, heuristic):
        self.puzzle = puzzle
        self.depth = depth
        self.heuristic = heuristic