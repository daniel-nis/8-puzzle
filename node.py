
class Node:
    
    def __init__(self, puzzle, depth, heuristic):
        self.puzzle = puzzle
        self.depth = depth
        self.heuristic = heuristic

        self.cost = self.depth + self.heuristic

    def __lt__(self, other):
        return (self.cost < other.cost)