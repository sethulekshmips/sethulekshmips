n = int(
    input("Number of queens and order of the board in which the game is going to be played is equal hence enter the "
          "number:"))
if n<4:
    print("The N-Queens problem only works for board having a minimum of 16 cells")
else:
    board = [[0 for i in range(n)] for i in range(n)]


    def column_check(board, row, column):
        for i in range(row, -1, -1):
            if board[i][column] == 1:
                return False
        return True
    def diagonal_check(board, row, column):
        for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(column, n)):
            if board[i][j] == 1:
                return False
        return True


    def N_QUEEN(board, row):
        if row == n:
            return True
        for i in range(n):
            if column_check(board, row, i) == True and diagonal_check(board, row, i) == True:
                board[row][i] = 1
                if N_QUEEN(board, row + 1):
                    return True
                board[row][i] = 0
        return False


    N_QUEEN(board, 0)

    for row in board:
        print(row)