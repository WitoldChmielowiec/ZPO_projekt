from src.board import Board, Disk


class TestBoardInitialization:
    def test_board_initialized_with_none(self):
        board = Board(None, None)
        for row in board.board:
            for cell in row:
                assert cell is None

    def test_board_dimensions(self):
        board = Board(None, None)
        assert len(board.board) == 6
        for row in board.board:
            assert len(row) == 7

    def test_current_player_initialization(self):
        board = Board("Player1", "Player2")
        assert board.current_player == "Player1"


class TestDropDisk:
    def test_drop_disk_successful(self):
        board = Board(None, None)
        diskR = Disk("R")
        diskY = Disk("Y")
        board.drop_disk(0, diskR)
        board.drop_disk(0, diskY)

        assert board.board[5][0] == diskR
        assert board.board[4][0] == diskY

    def test_drop_disk_full_column(self):
        board = Board(None, None)
        diskR = Disk("R")
        for _ in range(6):
            board.drop_disk(0, diskR)

        assert board.drop_disk(0, diskR) is False

    def test_drop_disk_invalid_column(self):
        board = Board(None, None)
        diskR = Disk("R")
        assert board.drop_disk(-1, diskR) is False
        assert board.drop_disk(7, diskR) is False
