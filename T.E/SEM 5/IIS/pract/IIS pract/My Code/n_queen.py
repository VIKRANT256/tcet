# Constraint
# Code: N Queens

def is_safe(board, row, col):
    N = len(board)
    
    # cheak column
    for i in range(row):
        if(board[i][col] == 1):
            return False
    
    # check diagonal
    c_backward = col 
    c_forward  = col 
    for i in range(row, -1, -1):
        if(board[i][c_backward] == 1 and i != row):
            return False
        
        if(c_backward == 0):
            break
        c_backward -= 1

    for i in range(row, -1, -1):
        if(board[i][c_forward] == 1 and i != row):
            return False
        
        if(c_forward == N-1):
            break
        c_forward += 1

    return True

def solve_n_queen(board, row = 0):
    N = len(board)
    if(row == N):
        return True
    for col in range(N):
        if(is_safe(board, row, col)):
            board[row][col] = 1
            if(solve_n_queen(board, row+1)):
                return True
            board[row][col] = 0
    return False


n = 8
board = []
for i in range(n):
    x = []
    for j in range(n):
        x.append(0)
    board.append(x)


solve_n_queen(board)
print(board)