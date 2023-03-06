import random

def makeGrid():
    """Returns a 3x3 grid."""
    return [[' ' for i in range(3)] for j in range(3)]

def printGrid(grid: list):
    """Formats the grid to make it more readable by looping and printing loop index."""
    print("    0    1    2")
    for x in range(len(grid)):
        print(x, grid[x], "\n")
    
def playerPlay(grid: list):
    """Function to input player's choice. Checks first if the line is empty, then check if the cell is empty.
    Calls itself if line, cell is full or input is out of range."""
    try:
        playerLine = int(input("Player's turn. Enter line: "))
        if ' ' not in grid[playerLine]:
            print("Please select an empty line.")
            playerPlay(grid)
        else:
            playerColumn = int(input("Enter column: "))
            if grid[playerLine][playerColumn] != ' ':
                print("Please select an empty cell.")
                playerPlay(grid)
            else:
                grid[playerLine][playerColumn] = 'X'
    except ValueError:
        print("Please enter a valid input.")
        playerPlay(grid)

    except IndexError:
        print("Number out of range. (0-2 included)")
        playerPlay(grid)

def computerPlay(grid: list):
    """Function to input computer's random choice. Loops over the grid to make list of empty cells first
    then picks a random one from that list."""
    validCases = []
    for x in range(len(grid)):
        for j in range(len(grid[x])):
            if grid[x][j] == ' ':
                validCases.append((x,j))
    computerMove = validCases[random.randint(0, len(validCases) -1)]
    computerLine, computerColumn = computerMove[0], computerMove[1]
    grid[computerLine][computerColumn] = 'O'

def checkplayerWinHor(grid: list):
    for x in range(len(grid)):
        if grid[x] == ['X', 'X', 'X']:
            return True
    return False

       
def checkcomputerWinHor(grid: list):
    for x in range(len(grid)):
        if grid[x] == ['O', 'O', 'O']:
            return True
    return False

def checkcomputerWinVert(grid: list):
    r = ''
    for x in range(len(grid)):
        for j in range(len(grid[x])):
            r += grid[j][x]
        
        if r == 'OOO':
            return True
        else:
            r = ''
    return False        

def checkplayerWinVert(grid: list):
    r = ''
    for x in range(len(grid)):
        for j in range(len(grid[x])):
            r += grid[j][x]
        if r == 'XXX':
            return True
        else:
            r = ''
    return False

def checkplayerWinDg(grid: list):
    #check for grid[j+1][x+1]
    r = ''
    for j in range(3):
        r += grid[j][j]
    
    if r == 'XXX':
        return True
    else:
        r = ''

    #check for grid[j-1][x+1]
    x = 3
    for j in range(x):
        x -= 1
        r += grid[j][x]
    return r == 'XXX'

def checkcomputerWinDg(grid: list):
    #check for grid[j+1][x+1]
    r = ''
    for j in range(len(grid)):
        r += grid[j][j]
    
    if r == 'OOO':
        return True
    else:
        r = ''

    #check for grid[j+][x-1]
    x = 3
    for j in range(x):
        x -= 1
        r += grid[j][x]
    return r == 'OOO'

def isDraw(grid: list):
    """Loops over the board, returns false if a cell is not used, returns True at the end of the loop."""
    for x in range(len(grid)):
        for j in range(len(grid[x])):
            if grid[x][j] == ' ':
                return False
    return True

if __name__ == "__main__":
    grid = makeGrid()
    printGrid(grid)
    while not isDraw(grid):
        if checkcomputerWinDg(grid) or checkcomputerWinHor(grid) or checkcomputerWinVert(grid):
            print("Computer wins!")
            break

        playerPlay(grid)
        if checkplayerWinDg(grid) or checkplayerWinHor(grid) or checkplayerWinVert(grid):
            print("Player wins!")
            break
        
        if isDraw(grid):
            print("Draw.")
            break
        computerPlay(grid)
        printGrid(grid)
    