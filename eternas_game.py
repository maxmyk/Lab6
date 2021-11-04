from math import e
from typing import List


def board_generation() -> List[list]:
    """
    Generates a game board of 16 x 4 size, i.e. two dimensional
    list (array) of 'g's, 'w's and '0's  that is used for the game.

    ### 16 x 4 | g - green, w - white, 0 - whitespace

    e.g. [[0,  0,   0,   0 ], [ 0,   0,   0,  'w'], [ 0,   0,  'g', 'g'], [0, 0, 'g', 'g'],
          [0, 'w', 'w', 'w'], [ 0,   0,  'w', 'g'], [ 0,   0,   0,  'g'], [0, 0, 'g', 'w'],
          [0, 'g', 'g', 'w'], [ 0,   0,   0,   0 ], ['w', 'g', 'w', 'w'], [0, 0,  0,  'g'],
          [0,  0,   0,  'g'], ['w', 'g', 'g', 'w'], [ 0,  'w', 'w', 'w'], [0, 0, 'g', 'w']]

    """
    from random import randrange
    white = 16
    green = 16
    board = [[] for _ in range(16)]
    for j in range(4):
        for i in range(16):
            if j == 0:
                randn = randrange(3)
                if randn == 1 and white > 0:
                    board[i].append('w')
                    white -= 1
                elif green > 0:
                    board[i].append('g')
                    green -= 1
                else:
                    board[i].append(0)
            else:
                randn = randrange(3)
                if randn == 1 and white > 0 and board[i][j-1] != 0:
                    board[i].append('w')
                    white -= 1
                elif randn == 2 and green > 0 and board[i][j-1] != 0:
                    board[i].append('g')
                    green -= 1
                else:
                    board[i].append(0)
    for i in range(16):
        board1 = board[i]
        board[i] = board1[::-1]
    return board


def winning_combination(board: List[list]) -> bool:
    """
    (list) -> bool

    Checks for winning combinations on the board.
    Returns a bool value of True and all winning positions if there is winning
    combination or False if not.

    >>> winning_combination(\
[[0, 'g', 'g', 'g'], [0, 'g', 'w', 'w'], [0, 0, 'g', 'g'], [0, 0, 0, 0],\
 [0, 0, 0, 'g'], [0, 0, 'w', 'w'], ['g', 'g', 'g', 'w'], [0, 0, 0, 0],\
 [0, 0, 'g', 'g'], [0, 'g', 'g', 'g'], ['w', 'g', 'w', 'w'], [0, 'g', 'w', 'g'],\
 [0, 0, 0, 0], [0, 0, 'g', 'g'], [0, 0, 0, 'w'], [0, 0, 'w', 'g']])
    False
    >>> winning_combination(\
[[0, 'g', 'g', 'w'], [0, 0, 0, 0], [0, 0, 0, 0], ['g', 'g', 'g', 'w'],\
 [0, 0, 'w', 'g'], [0, 0, 'g', 'g'], [0, 0, 0, 'w'], ['w', 'g', 'g', 'g'],\
 ['w', 'w', 'g', 'w'], [0, 0, 0, 'w'], [0, 'w', 'g', 'g'], [0, 0, 0, 0],\
 [0, 0, 0, 0], [0, 'g', 'w', 'w'], [0, 0, 'w', 'g'], [0, 0, 'w', 'g']])
    False
    >>> winning_combination(\
[['w', 'g', 'g', 'w'], [0, 0, 0, 0], [0, 'g', 'w', 'g'], ['g', 'w', 'w', 'w'],\
 [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 0, 0], [0, 0, 'w', 'w'],\
 ['w', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'],\
 [0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 0, 'g']])
    False
    >>> winning_combination(\
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 'w', 'g'], [0, 0, 0, 'g'],\
 ['g', 'g', 'g', 'w'], [0, 0, 'g', 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'g'],\
 [0, 0, 'w', 'w'], [0, 'w', 'w', 'g'], ['g', 'w', 'g', 'g'], [0, 0, 0, 0],\
 [0, 0, 0, 'w'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'w']])
    False
    >>> winning_combination(\
[[0, 'g', 'g', 'w'], [0, 0, 'w', 'g'], ['g', 'g', 'w', 'g'], [0, 0, 0, 'w'],\
 [0, 0, 0, 'w'], ['w', 'g', 'w', 'w'], [0, 'w', 'g', 'g'], [0, 0, 0, 'w'],\
 [0, 0, 0, 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'w'], [0, 0, 0, 0],\
 [0, 0, 0, 0], ['g', 'w', 'g', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 'g']])
    (True, [[(3, 7), (3, 8), (3, 9), (3, 10)]])
    >>> winning_combination(\
[[0, 'w', 'w', 'w'], [0, 0, 0, 'w'], [0, 'w', 'g', 'w'], [0, 0, 0, 0],\
 [0, 0, 0, 0], [0, 0, 0, 'g'], ['w', 'w', 'w', 'g'], [0, 0, 'w', 'g'],\
 [0, 0, 0, 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'g'], [0, 0, 0, 'g'],\
 [0, 0, 'g', 'w'], [0, 'g', 'w', 'g'], ['g', 'g', 'w', 'g'], ['w', 'g', 'w', 'g']])
    (True, [[(3, 5), (3, 6), (3, 7), (3, 8)], [(2, 13), (2, 14), (2, 15), (2, 0)],\
 [(0, 11), (1, 12), (2, 13), (3, 14)]])
    >>> winning_combination(\
[[0, 0, 'g', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 0],\
 [0, 0, 0, 0], [0, 0, 0, 'g'], ['w', 'w', 'g', 'g'], ['w', 'w', 'g', 'g'],\
 ['w', 'g', 'g', 'w'], [0, 'g', 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'g'],\
 [0, 0, 0, 'g'], [0, 'g', 'w', 'w'], [0, 0, 0, 'w'], [0, 0, 'g', 'g']])
    (True, [[(3, 9), (3, 10), (3, 11), (3, 12)]])
    >>> winning_combination(\
[[0, 0, 'w', 'w'], [0, 0, 'w', 'w'], ['g', 'g', 'g', 'w'], [0, 'w', 'g', 'g'],\
 ['g', 'g', 'w', 'w'], [0, 0, 0, 'w'], [0, 0, 'w', 'w'], [0, 0, 'g', 'w'],\
 [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 'w', 'w', 'w'],\
 ['g', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 0], [0, 0, 'w', 'w']])
    (True, [[(3, 4), (3, 5), (3, 6), (3, 7)], [(3, 15), (3, 0), (3, 1), (3, 2)]])
    >>> winning_combination(\
[['g', 'w', 'w', 'w'], [0, 'g', 'g', 'w'], [0, 0, 'w', 'w'], [0, 'g', 'w', 'w'],\
 [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 'w', 'g'], [0, 0, 0, 'g'],\
 [0, 0, 0, 0], [0, 'w', 'w', 'w'], ['w', 'w', 'w', 'g'], [0, 0, 0, 0],\
 [0, 0, 0, 'g'], [0, 0, 'g', 'g'], ['g', 'w', 'w', 'w'], [0, 0, 'g', 'w']])
    (True, [[(3, 0), (3, 1), (3, 2), (3, 3)], [(3, 14), (3, 15),\
 (3, 0), (3, 1)], [(3, 15), (3, 0), (3, 1), (3, 2)]])
    """
    combination = []
    for i in range(16):
        if board[i].count('w') == 4 or board[i].count('g') == 4:
            combination.append([(0, i), (1, i), (2, i), (3, i)])
    for i in range(16):
        for j in range(4):
            if board[i][j] == board[(i+1) % 16][j] == board[(i+2) % 16][j] == board[(i+3) % 16][j] != 0:
                combination.append(
                    [(j, i), (j, (i+1) % 16), (j, (i+2) % 16), (j, (i+3) % 16)])
    for i in range(16):
        if board[i][3] == board[(i+1) % 16][2] == board[(i+2) % 16][1] == board[(i+3) % 16][0] != 0:
            combination.append(
                [(0, i), (1, (i+1) % 16), (2, (i+2) % 16), (3, (i+3) % 16)])
    for i in range(16):
        if board[i][0] == board[(i+1) % 16][1] == board[(i+2) % 16][2] == board[(i+3) % 16][3] != 0:
            combination.append(
                [(3, i), (2, (i+1) % 16), (1, (i+2) % 16), (0, (i+3) % 16)])
    ans = False
    if combination:
        ans = (True, combination)
    return ans


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
