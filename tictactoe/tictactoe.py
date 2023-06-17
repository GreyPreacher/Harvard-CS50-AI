"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count, O_count = 0, 0
    for h in board:
        for cell in h:
            X_count += (cell == X)
            O_count += (cell == O)
    return X if X_count == O_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.append((i, j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    loc = player(board)
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("The location is not EMPTY")
    new_board[i][j] = loc
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != EMPTY:
            return board[i][0]
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != EMPTY:
            return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != EMPTY:
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for h in board:
        for cell in h:
            if cell == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0


def argmax(v):
    ix = 0
    maxX = v[0]
    for i, x in enumerate(v):
        if x > maxX:
            ix, maxX = i, x
    return ix


def argmin(v):
    ix = 0
    minX = v[0]
    for i, x in enumerate(v):
        if x < minX:
            ix, minX = i, x
    return ix


def min_value(board):
    if terminal(board):
        return utility(board)
    v = 10
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -10
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    X : Max
    O : Min
    """
    if terminal(board):
        return None
    Actions = actions(board)
    turn = player(board)
    v = []
    if turn == X:
        for action in Actions:
            v.append(min_value(result(board, action)))
        return Actions[argmax(v)]
    if turn == O:
        for action in Actions:
            v.append(max_value(result(board, action)))
        return Actions[argmin(v)]