"""
Główny plik aplikacji.
"""

import board
import players


def main():
    B = board.Board(
        players.HumanPlayer("Gracz 1", "R"), players.HumanPlayer("Gracz 2", "Y")
    )

    while not B.is_board_full() and B.check_winner() is None:
        B.next_move()
        print(B)

    if B.check_winner() is not None:
        print(f"Gratulacje! {B.check_winner()} wygrał!")
    else:
        print("Remis!")


if __name__ == "__main__":
    main()
