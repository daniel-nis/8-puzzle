from node import Node
import copy

# using the professor's method of getting the puzzle, as seen in the project slides
def get_puzzle():
    print("Enter your puzzle, using a zero to represent the blank. " 
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



    puzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]
    print_puzzle(puzzle)

    #puzzle.insert(2, [1, 2, 3])

    #puzzle[0][2] = user_puzzle[2][0]      # how to swap

    #find_blank(puzzle)
    #up(puzzle)
    #print_puzzle(puzzle)

    #down(puzzle)
    #print_puzzle(puzzle)

    #left(puzzle)
    #print_puzzle(puzzle)

    #right(puzzle)
    #print_puzzle(puzzle)

    movements(puzzle)

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
                #print(i,"\n")
                #print(j,"\n")
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
        #up_node = Node(moved_up, 0, 0)
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
    depth = 0

    if(up(puzzle) != -1):
        movements.append(up(puzzle))
        print_puzzle(up(puzzle))
    
    if(down(puzzle) != -1):
        movements.append(down(puzzle))
        print_puzzle(down(puzzle))
    
    if(left(puzzle) != -1):
        movements.append(left(puzzle))
        print_puzzle(left(puzzle))

    if(right(puzzle) != -1):
        movements.append(right(puzzle))
        print_puzzle(right(puzzle))

    h = misplaced_tiles(puzzle)
    print(h)

    h2 = manhattan_distance(puzzle)
    print(h2)

    #print(movements)
    #print(depth)

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


get_puzzle()

# implement a priority queue for the moves

# search algorithm
# function general-search(problem, QUEUEING-FUNCTION)
# nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
# loop do
#    if EMPTY(nodes) then return "failure"
#        node = REMOVE-FRONT(nodes)
#    if problem.GOAL-TEST(node.STATE) succeeds then return node
#        nodes = QUEUEING-FUNCTION(nodes, EXPAND(node, problem.OPERATORS))
# end