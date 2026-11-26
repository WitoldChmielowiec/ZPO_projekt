from src.board import Disk


class TestDiskColor:
    def test_disk_initialization(self):
        disk = Disk("R")
        assert disk.color == "R"

    def test_disk_equality(self):
        diskR1 = Disk("R")
        diskR2 = Disk("R")
        diskY = Disk("Y")
        assert diskR1 == diskR2
        assert diskR1 != diskY
        assert diskR1 != "R"


class TestDiskRepresentation:
    def test_disk_repr(self):
        disk = Disk("R")
        assert repr(disk) == "Disk(R)"

    def test_disk_str(self):
        disk = Disk("Y")
        assert str(disk) == "Y"
