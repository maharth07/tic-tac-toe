import math

# Constants for the players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    """Prints the current state of the board."""
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3 + 1]} | {board[i*3 + 2]} ")
        if i < 2:
            print("---+---+---")
    print()

def check_winner(board):
    """Checks if there is a winner and returns the winning symbol, or None."""
    # All possible winning combinations
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for combo in win_states:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != EMPTY:
            return board[combo[0]]
    
    if EMPTY not in board:
        return 'TIE' # Board is full, it's a tie
        
    return None # Game is still ongoing

def minimax(board, depth, is_maximizing, alpha, beta):
    """
    The Minimax algorithm with Alpha-Beta pruning.
    Evaluates all possible future moves to find the best possible outcome.
    """
    winner = check_winner(board)
    
    # Base cases: return a heuristic score if the game is over
    if winner == AI:
        return 10 - depth  # Prefer faster wins
    elif winner == HUMAN:
        return depth - 10  # Prefer slower losses
    elif winner == 'TIE':
        return 0
        
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI  # Make a temporary move
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY # Undo the move
                
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                
                # Alpha-Beta Pruning
                if beta <= alpha:
                    break 
        return best_score
        
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN  # Make a temporary move
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = EMPTY # Undo the move
                
                best_score = min(score, best_score)
                beta = min(beta, score)
                
                # Alpha-Beta Pruning
                if beta <= alpha:
                    break
        return best_score

def get_best_move(board):
    """Finds the optimal move for the AI using the minimax algorithm."""
    best_score = -math.inf
    best_move = None
    
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI # Try this move
            # Start minimax assuming it will be the human's turn next (False)
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = EMPTY # Undo the move
            
            if score > best_score:
                best_score = score
                best_move = i
                
    return best_move

def play_game():
    """Main game loop."""
    board = [EMPTY] * 9
    print("Welcome to Tic-Tac-Toe against the AI!")
    print("Positions are 0-8, starting from top-left to bottom-right.")
    print_board([str(i) for i in range(9)]) # Show position numbers
    
    while True:
        # Human's Turn
        valid_move = False
        while not valid_move:
            try:
                move = int(input("Enter your move (0-8): "))
                if move < 0 or move > 8 or board[move] != EMPTY:
                    print("Invalid move. Try again.")
                else:
                    board[move] = HUMAN
                    valid_move = True
            except ValueError:
                print("Please enter a valid number.")
                
        print_board(board)
        if check_winner(board):
            break
            
        # AI's Turn
        print("AI is thinking...")
        ai_move = get_best_move(board)
        if ai_move is not None:
            board[ai_move] = AI
            
        print_board(board)
        if check_winner(board):
            break

    # Announce the results
    winner = check_winner(board)
    if winner == 'TIE':
        print("It's a Tie!")
    else:
        print(f"The winner is {winner}!")

if __name__ == "__main__":
    play_game()