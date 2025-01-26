# The Game Board
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    board[position] = mark
    return board

# TODO: print the game board as described at the top of this code skeleton
def printBoard():
    print("\n")
    print("\t" + board[1] + " | " + board[2] + " | " + board[3])
    print("\t---------")
    print("\t" + board[4] + " | " + board[5] + " | " + board[6])
    print("\t---------")
    print("\t" + board[7] + " | " + board[8] + " | " + board[9])
    print("\n")

# TODO: check for wrong input, this function should return True or False
def validateMove(position):
    position = int(position)
    if position < 1 or position > 9:
        return False
    elif board[position] == 'X' or board[position] == 'O':
        return False
    return True

# TODO: list out all the combinations of winning, you will need this
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 5, 9],
    [3, 5, 7],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

# TODO: implement a logic to check if the previous winner just win
def checkWin(player):
    mark_list = [k for k, v in board.items() if v == player]
    for combination in winCombinations:
        if all(pos in mark_list for pos in combination):
            return True
    return False

# TODO: implement a function to check if the game board is already full
def checkFull():
    return all(v == 'X' or v == 'O' for v in board.values())

# Game logic
gameEnded = False
currentTurnPlayer = 'X'

# Entry point of the whole program
print('Game started: \n\n' +
      ' 1 | 2 | 3 \n' +
      ' --------- \n' +
      ' 4 | 5 | 6 \n' +
      ' --------- \n' +
      ' 7 | 8 | 9 \n')

while not gameEnded:
    move = input(f"{currentTurnPlayer}'s turn, input (1-9): ")

    # Validate the move input
    if not validateMove(move):
        print("Invalid move. Try again.")
        continue

    # Update the board
    markBoard(int(move), currentTurnPlayer)
    printBoard()

    # Check if the current player has won
    if checkWin(currentTurnPlayer):
        print(f"\nGame Over! {currentTurnPlayer} player won!\n")
        gameEnded = True
        continue

    # Check if the board is full (tie)
    if checkFull():
        print("\nGame Over! It's a tie!\n")
        gameEnded = True
        continue

    # Switch to the other player
    currentTurnPlayer = 'O' if currentTurnPlayer == 'X' else 'X'

    # Ask for restart if the game is over
    if gameEnded:
        restart_choice = input("Do you want to restart the game? (y/n): ")
        if restart_choice.lower() == 'y':
            # Reset board and start a new game
            for k in board.keys():
                board[k] = ' '
            gameEnded = False
            currentTurnPlayer = 'X'
            print('Game restarted!')
            printBoard()
        else:
            print("Thanks for playing!")
            break