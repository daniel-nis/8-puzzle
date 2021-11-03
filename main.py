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

    #puzzle.insert(2, [1, 2, 3])

    #puzzle[0][2] = user_puzzle[2][0]      # how to swap

    find_blank(puzzle)
    #up(puzzle)
    print(puzzle)

# for moving up,down,left,right create borders (left border, top border etc.)
# create function to find location of 0
# movement functions will use 0 location to tell if a move is possible
# create a temp value to hold the value of the intended movement OR find way to switch the values of the 0 and intended new spot 

# finds the location of 0 (the blank)
def find_blank(puzzle):
    # search the matrix to find 0 location
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                #print(i,"\n")
                #print(j,"\n")
                return i, j

def up(puzzle):
    # move 0 up a row, unless 0 is in topmost row
    for i in puzzle:
        if puzzle[i] != 0:
            print("hjjj")

get_puzzle()