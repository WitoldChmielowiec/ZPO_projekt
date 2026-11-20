"""
Plik odpowiedzialny za implementację planszy gry.
"""

import abc  # noqa: F401

import pygame  # noqa: F401

import players  # noqa: F401


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

    def __eq__(self, other):
        if isinstance(other, Disk):
            return self.color == other.color
        return False


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

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True

    def check_winner(self):
        # wiesze
        for row in self.board:
            for i in range(4):
                if (
                    row[i] is not None
                    and row[i] == row[i + 1] == row[i + 2] == row[i + 3]
                ):
                    return row[i]

        # kolumny
        for col in range(7):
            for row in range(3):
                if (
                    self.board[row][col] is not None
                    and self.board[row][col]
                    == self.board[row + 1][col]
                    == self.board[row + 2][col]
                    == self.board[row + 3][col]
                ):
                    return self.board[row][col]

        # przekatne
        for row in range(3):
            for col in range(4):
                if (
                    self.board[row][col] is not None
                    and self.board[row][col]
                    == self.board[row + 1][col + 1]
                    == self.board[row + 2][col + 2]
                    == self.board[row + 3][col + 3]
                ):
                    return self.board[row][col]
                if (
                    self.board[row][6 - col] is not None
                    and self.board[row][6 - col]
                    == self.board[row + 1][5 - col]
                    == self.board[row + 2][4 - col]
                    == self.board[row + 3][3 - col]
                ):
                    return self.board[row][6 - col]

        return None

    def draw(self, surface):
        raise NotImplementedError("TODO")

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        out = ""
        for row in self.board:
            out += (
                " | ".join(
                    f"{str(cell) if cell is not None else ' ':^10}" for cell in row
                )
                + "\n"
            )
        return out


board = Board(1, 2)
board.drop_disk(0, Disk("red"))
board.drop_disk(0, Disk("yellow"))
board.drop_disk(1, Disk("yellow"))
board.drop_disk(2, Disk("yellow"))
board.drop_disk(3, Disk("yellow"))
board.drop_disk(4, Disk("yellow"))
is_winner = board.check_winner()

print(board)
print(is_winner)
