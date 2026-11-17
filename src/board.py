"""
Plik odpowiedzialny za implementację planszy gry.
"""

import abc
import pygame
import players


class Disk:
    def __init__(self, color):
        self.color = color

    # TODO
    def draw(self, surface, position):
        raise NotImplementedError("TODO")

    def __str__(self):
        return self.color

    def __repr__(self):
        return self.color


class Board:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[None for _ in range(7)] for _ in range(6)]

    def drop_disk(self, column, disk):
        for row in reversed(range(6)):
            if self.board[row][column] is None:
                self.board[row][column] = disk
                return True
        return False

    def is_board_valid(self):
        raise NotImplementedError("TODO")

    def is_board_full(self):
        raise NotImplementedError("TODO")

    def check_winner(self):
        raise NotImplementedError("TODO")

    def draw(self, surface):
        raise NotImplementedError("TODO")

    def __str__(self):
        raise NotImplementedError("TODO")

    def __repr__(self):
        raise NotImplementedError("TODO")


board = Board(1, 2)
board.drop_disk(0, Disk("red"))
board.drop_disk(0, Disk("yellow"))

print(board.board)
