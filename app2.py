import random

def convertBoard(board):
    global boardS
    boardPrint = []
    for i in range(0, len(board), boardS):
        boardPrint.append(board[i:i + boardS])
    return boardPrint

def printBoard(): #prints the board nicely
    boardPrint = convertBoard(board)
    for i in boardPrint:
        print(str(i))

def nextPlayer(currentPlayer,amount): #Alternates between players
    if(currentPlayer >= amount):
        currentPlayer = 1
    else:
        currentPlayer += 1
    return currentPlayer

winName = ""
def listEqual(name): #Checks if all elements of a list are equal
    global playing,winName
    winName = name
    if name.count(name[0]) == len(name) and name[0] != 0:
        return True
    return False

def win(board): #Checks every way a player could win. Diagonally, vertically or horizontally.
    #Diagonal right
    #print("hi")
    #print(board)
    diagonal = []
    for ir in range(len(board)):
        diagonal.append(board[ir][ir])
    if listEqual(diagonal):
        return True
    #Diagonal left
    cols = list(reversed(range(len(board))))
    diagonal = []
    for il in range(len(board)):
        diagonal.append(board[il][cols[il]])
    if listEqual(diagonal):
        return True
    #Vertical
    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if listEqual(check):
            return True
    #Horizontal
    for row in board:
        if listEqual(row):
            return True
    
    return False

def compMove(boardF):
    global board
    possibleMoves = [index for index, letter in enumerate(boardF) if(letter == 0)]
    for i in possibleMoves:
        boardCopy = board[:]
        boardCopy[i] = "X"
        #print(boardCopy)
        if win(convertBoard(boardCopy)):
            return i

    for i in possibleMoves:
        boardCopy = board[:]
        boardCopy[i] = "O"
        #print(i)
        if win(convertBoard(boardCopy)):
            return i

    """
    print("RANDOM IT IS")
    print(len(possibleMoves))
    print(possibleMoves)
    print(possibleMoves[random.randint(0,len(possibleMoves) - 1 )])
    """
    return possibleMoves[random.randint(0,len(possibleMoves) - 1)]
    



#make board
while True:
    try:
        boardS = int(input("Board size: "))
        if boardS >= 2:
            break
    except:
        continue

board = []
for i in range(boardS**2):
    board.append(0)

print(board)

printBoard()

while True:
    try:   
        amount = int(input("How many players: "))
        if amount >= 1:
            break
    except:
        continue

players = []
if(amount == 1):
    players = ["O"]
elif(amount == 2):
    players = ["O","X"]
else:
    for i in range(amount):
        players.append(input(f"Choose the mark for player {i}: "))

currentPlayer = 1
playing = True

while playing: #Play loop
    correctCheck = True
    while True:
        try:
            edit = int(input("Position: ")) - 1 #Starts at 1
        except:
            continue
        possibleMovesPlayer = [index for index, letter in enumerate(board) if(letter == 0)]
        if(type(edit) == type(1)):
            if possibleMovesPlayer.count(edit) != 0:
                break
            else:
                print(f"Invalid input, pick a position between 1 and {boardS**2}.")
        elif(edit == "exit"):
                exit()
        elif(edit == 'quit'):
            exit()
        else:
            print("Invalid input, type a number.")
    
    board[edit] = players[currentPlayer - 1]
    printBoard()
    #print(board)
    


    currentPlayer = nextPlayer(currentPlayer,amount)

    if(len([index for index, letter in enumerate(board) if(letter == 0)]) == 0):
            print("Tie!")
            exit()

    if amount <= 1:
        board[compMove(board)] = "X"
        printBoard()

    if(win(convertBoard(board))):
        print(f"The winner is {winName[0]}!")
        playing = False #Stops the game

