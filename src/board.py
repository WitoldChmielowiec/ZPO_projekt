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


class Board:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[None for _ in range(7)] for _ in range(6)]
