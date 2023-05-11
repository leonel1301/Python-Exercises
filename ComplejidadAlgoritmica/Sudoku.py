import numpy as np


def check(a):
    found = [False] * 9
    for x in a:
        found[x - 1] = True
    return sum(found) == 9


def checkSudoku(board):
    for i in range(9):
        if not check(board[i]):
            return False
        if not check(board[:, i]):
            return False
        a, b = i // 3, i % 3
        if not check(board[a * 3:(a + 1) * 3, b * 3:(b + 1) * 3].reshape((9))):
            return False
    return True


a = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
              [4, 5, 6, 7, 8, 9, 1, 2, 3],
              [7, 8, 9, 1, 2, 3, 4, 5, 6],
              [2, 3, 4, 5, 6, 7, 8, 9, 1],
              [6, 6, 7, 8, 9, 1, 2, 3, 4],
              [8, 9, 1, 2, 3, 4, 5, 6, 7],
              [3, 4, 5, 6, 7, 8, 9, 1, 2],
              [5, 7, 8, 9, 1, 2, 3, 4, 5],
              [9, 1, 2, 3, 4, 5, 6, 7, 8]])
print(checkSudoku(a))
