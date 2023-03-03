import numpy as np

ROW_COUNT = 6
COL_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COL_COUNT))
    return board

def drop_piece(board, rol, col, piece):
    board[row][col] = piece    

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    #check horizontal positions for win
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    
    #check vertical positions for win
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    #check for positive slope diagonals
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    #check for neg slope diagonals
    for c in range(COL_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
            

board = create_board()
game_over = False
turn = 0


while not game_over:
    #ask player 1 input
    if turn == 0:
        col = int(input("Player 1's turn (0-6): "))
        #code to make sure player enters a valid input

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
        else:
            print("Invalid Move")
            turn -=1

            if winning_move(board, 1):
                print("Player 1 wins! Congrats!")
                game_over = True


    #ask player 2 input
    else:
        col = int(input("Player 2's turn (0-6): "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
        else:
            print("Invalid Move")
            turn -=1

            if winning_move(board, 1):
                print("Player 1 wins! Congrats!")
                game_over = True

    print_board(board)

    turn +=1
    turn  = turn % 2