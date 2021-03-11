import numpy as np


class Player:
    def __init__(self, nr, symbol):
        self.nr = nr
        self.symbol = symbol
        self.score = 0

    @property
    def verbose_name(self):
        return f'P{str(self.nr)} ({self.symbol}) : '


class Board:
    def __init__(self):
        self.matrix = np.zeros((3, 3), dtype='int8')

    def reset_matrix(self):
        self.matrix = np.zeros((3, 3), dtype='int8')


def check_for_winner(board):
    """If there's a winner, returns the number of the player, else returns None"""
    for i in range(3):

        row = board[i, :]
        if 0 not in row and sum(row) in (3, 6):
            return sum(row) // 3

        col = board[:, i]
        if 0 not in col and sum(col) in (3, 6):
            return sum(col) // 3

    diagonal = board.diagonal()
    if 0 not in diagonal and sum(diagonal) in (3, 6):
        return sum(diagonal) // 3

    secondary_diagonal = board[::-1].diagonal()
    if 0 not in secondary_diagonal and sum(secondary_diagonal) in (3, 6):
        return sum(secondary_diagonal) // 3

    return
