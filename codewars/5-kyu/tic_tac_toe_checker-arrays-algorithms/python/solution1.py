def checking_free_square(board):
    for square in board:
        for s in square:
            if s == 0:
                return True
    return False


def checking_state_for(n, board):
    
    # Horizontal
    for x in range(3):
        horizontal = 0
        for y in range(3):
            if board[x][y] == n:
                horizontal += 1
            if horizontal == 3:      
                return True
            
    # Vertical   
    for x in range(3):
        vertical = 0
        for y in range(3):
            if board[y][x] == n:
                vertical += 1
            if vertical == 3:      
                return True
            
    # Obliquely \
    obliquely1 = 0
    for idx, square in enumerate(board):
        if board[idx][idx] == n:
            obliquely1 += 1
        if obliquely1 == 3:
            return True 
        
    # Obliquely /
    obliquely2 = 0
    for x in reversed(range(2, -1, -1)):
        if board[x][x] == n:
            obliquely2 += 1
        if obliquely2 == 3:
            return True
        
    return False

def checking_condition(X, O, free):
    if X and not O:
        return 1
    elif not X and O:
        return 2
    elif not X and not O and free:
        return -1
    elif not X and not O and not free:
        return 0
    
def is_solved(board):
        
    free_square = checking_free_square(board)
    X_square = checking_state_for(1, board)
    O_square = checking_state_for(2, board)

    result = checking_condition(X_square, O_square, free_square)
    return result

def checking_free_square(board):
    for square in board:
        for s in square:
            if s == 0:
                return True
    return False


def checking_state_for(n, board):
    
    # Horizontal
    for x in range(3):
        horizontal = 0
        for y in range(3):
            if board[x][y] == n:
                horizontal += 1
            if horizontal == 3:      
                return True
            
    # Vertical   
    for x in range(3):
        vertical = 0
        for y in range(3):
            if board[y][x] == n:
                vertical += 1
            if vertical == 3:      
                return True
            
    # Obliquely \
    obliquely1 = 0
    for idx, square in enumerate(board):
        if board[idx][idx] == n:
            obliquely1 += 1
        if obliquely1 == 3:
            return True 
        
    # Obliquely /
    for idx, square in enumerate(reversed(board)):
        print(board[idx][idx], end = " ")
    print()
    return False

def checking_condition(X, O, free):
    if X and not O:
        return 1
    elif not X and O:
        return 2
    elif not X and not O and free:
        return -1
    elif not X and not O and not free:
        return 0
    
def is_solved(board):
        
    free_square = checking_free_square(board)
    X_square = checking_state_for(1, board)
    O_square = checking_state_for(2, board)

    result = checking_condition(X_square, O_square, free_square)
    return result
