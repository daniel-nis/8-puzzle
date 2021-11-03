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

    print(puzzle)

get_puzzle()

# for moving up,down,left,right create borders (left border, top border etc.)
# create function to find location of 0
# movement functions will use 0 location to tell if a move is possible
# create a temp value to hold the value of the intended movement OR find way to switch the values of the 0 and intended new spot 

#def find_blank():
    # search matrix to find 0

#def up():
    # move 0 up a row, unless 0 is in topmost row