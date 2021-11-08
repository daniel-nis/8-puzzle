from node import Node
import copy
import heapq

# using the professor's method of getting the puzzle, as seen in the project slides
def get_puzzle():
    """print("Enter your puzzle, using a zero to represent the blank. " 
            + "Please only enter valid 8-puzzles. Enter the puzzle demilimiting " 
            + "the numbers with a space. RET only when finished." + '\n')

    puzzle_row_one = input("Enter the first row: ")
    puzzle_row_two = input("Enter the second row: ")
    puzzle_row_three = input("Enter the third row: ")

    puzzle_row_one = puzzle_row_one.split()
    puzzle_row_two = puzzle_row_two.split()
    puzzle_row_three = puzzle_row_three.split()
    
    for i in range(0, 3):
        puzzle_row_one[i] = int(puzzle_row_one[i])
        puzzle_row_two[i] = int(puzzle_row_two[i])
        puzzle_row_three[i] = int(puzzle_row_three[i])



    puzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]"""
    #puzzle = [[1, 2, 3], [5, 0, 6], [4, 7, 8]]        # depth 4          ##### comment out later #####
    #puzzle = [[1, 3, 6], [5, 0, 2], [4, 7, 8]]          # depth 8
    #puzzle = [[1, 3, 6], [5, 0, 7], [4, 8, 2]]          # depth 12
    #puzzle = [[1, 6, 7], [5, 0, 3], [4, 8, 2]]          # depth 16
    #puzzle = [[7, 1, 2], [4, 8, 5], [6, 3, 0]]         # depth 20
    puzzle = [[0, 7, 2], [4, 6, 1], [3, 5, 8]]          # depth 24
    #print_puzzle(puzzle)

    general_search(puzzle)

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# for moving up,down,left,right create borders (left border, top border etc.)
# movement functions will use 0 location to tell if a move is possible
# if move is possible, switch the values of the 0 and the moved tile

# finds the location of 0 (the blank)
def find_blank(puzzle):
    # search the matrix to find 0 location
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

def print_puzzle(puzzle):
    for i in range(3):
        print(puzzle[i])
    print("\n")

def up(puzzle):
    # move 0 up a row, unless 0 is in topmost row
    moved_up = copy.deepcopy(puzzle)    # make copy of puzzle to not change original puzzle
    row, col = find_blank(moved_up)

    if (row != 0):
        moved_up[row][col] = moved_up[row-1][col]   # swap the 0 with top value
        moved_up[row-1][col] = 0
    else:
        return -1
    return moved_up
    #return up_node

def down(puzzle):
    # move 0 down a row, unless 0 is in bottommost row
    moved_down = copy.deepcopy(puzzle)
    row, col = find_blank(moved_down)

    if (row != 2):
        moved_down[row][col] = moved_down[row+1][col]
        moved_down[row+1][col] = 0
    else:
        return -1
    return moved_down

def left(puzzle):
    # move 0 to the left, unless 0 is in leftmost row
    moved_left = copy.deepcopy(puzzle)
    row, col = find_blank(moved_left)

    if (col != 0):
        moved_left[row][col] = moved_left[row][col-1]
        moved_left[row][col-1] = 0
    else:
        return -1
    return moved_left

def right(puzzle):
    # move 0 to the right, unless 0 is in rightmost row
    moved_right = copy.deepcopy(puzzle)
    row, col = find_blank(moved_right)

    if (col != 2):
        moved_right[row][col] = moved_right[row][col+1]
        moved_right[row][col+1] = 0
    else:
        return -1
    return moved_right

# movements function should keep track of each possible movement made, adding 1 to the depth for each iteration
def movements(puzzle):
    movements = []

    if(up(puzzle) != -1):
        movements.append(up(puzzle))
    
    if(down(puzzle) != -1):
        movements.append(down(puzzle))
    
    if(left(puzzle) != -1):
        movements.append(left(puzzle))

    if(right(puzzle) != -1):
        movements.append(right(puzzle))

    return movements

# misplaced tile heuristic finder will count the number of tiles
# that are not in their correct spot

def misplaced_tiles(puzzle):
    h = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != goal[i][j]:
                if puzzle[i][j] != 0:
                    h += 1
    return h

# manhattan distance heuristic finder counts the number of spots that
# a tile is off from its goal, and totals up this count for all tiles
# equation: h = |x1 - x2| + |y1 - y2|

def manhattan_distance(puzzle):
    h = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != goal[i][j]:
                if puzzle[i][j] != 0:       
                    goal_row, goal_col = get_goal_tile(puzzle[i][j])
                    row = i
                    col = j
                    h += abs(goal_row - row) + abs(goal_col - col)
    return h

# gets the goal location of the tile being looked at in the manhattan distance function
def get_goal_tile(tile):
    for i in range(3):
        for j in range(3):
            if goal[i][j] == tile:
                return i, j

# gets the selection for the chosen algorithm
def search_selection():
    print("Enter the number associated with an algorithm to select it:\n"
                + "1. Uniform Cost Search\n"
                + "2. A* with Misplaced Tile heuristic\n"
                + "3. A* with Manhattan Distance heuristic")
    selection = input("Enter number: ")
    return selection

# utilizes a priority queue that determines priority based on cost
# terminates if the depth exceeds 500, or if the queue is ever empty
def general_search(puzzle):
    already_visited = []

    selection = search_selection()
    if selection == '1':
        h = 0
    elif selection == '2':
        h = misplaced_tiles(puzzle)
    elif selection == '3':
        h = manhattan_distance(puzzle)
    heuristic = h
    depth = 0

    starting_node = Node(puzzle, depth, heuristic)
    nodes = []  # priority queue
    nodes.append(starting_node)
    
    nodes_expanded = 0
    max_queue_size = 0

    goal_reached = False
    while goal_reached != True:             ### loop ###

        if len(nodes) == 0:
            return "failure"

        heapq.heapify(nodes)
        node = heapq.heappop(nodes)

        stdout = open("output.txt", "w")
        print("The best state to expand with a g(n) = ", node.depth, " and h(n) = ", node.heuristic, " is ")
        print_puzzle(node.puzzle)

        if node.puzzle == goal:
            print("Goal has been reached.")
            print_puzzle(node.puzzle)
            print("Depth: ", node.depth)
            print("Nodes Expanded: ", nodes_expanded)
            print("Max Queue Size: ", max_queue_size)
            goal_reached = True

        elif node.depth >= 500:
            print("\nThe depth has surpassed 500, puzzle must be invalid.\n")
            break

        else:
            moves = movements(node.puzzle)

            depth = node.depth
            nodes_expanded += len(moves)

            for k in range(len(moves)):
                if selection == '1':
                    heuristic = 0
                elif selection == '2':
                    heuristic = misplaced_tiles(moves[k])
                elif selection == '3':
                    heuristic = manhattan_distance(moves[k])
                new_node = Node(moves[k], depth, heuristic)
                new_node.depth = depth+1
                if new_node.puzzle not in already_visited:
                    already_visited.append(new_node.puzzle)
                    heapq.heappush(nodes, new_node)
            
        max_queue_size = max(len(nodes), max_queue_size)

get_puzzle()