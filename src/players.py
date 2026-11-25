"""
Plik odpowiedzialny za implementacji klas graczy, w tym gracza ludzkiego oraz gracza komputerowego.
"""

from board import Disk


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_move(self, board):
        raise NotImplementedError("Subclass")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Player(name={self.name}, color={self.color})"


class HumanPlayer(Player):
    def make_move(self, board):
        column = int(input(f"{self.name}, wybierz kolumnę (0-6): "))
        while column < 0 or column > 6 or not board.drop_disk(column, Disk(self.color)):
            print("Nieprawidłowy ruch. Spróbuj ponownie.")
            column = int(input(f"{self.name}, wybierz kolumnę (0-6): "))
        print(f"{self.name} umieścił dysk w kolumnie {column}.")
