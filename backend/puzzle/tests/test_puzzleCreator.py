import pytest
from src.puzzleCreator import *


# test number of puzzle
def test_number_of_pieces():
    p = Puzzle('images/Python_(programming_language).png', 30, 'test')
    assert len(p.pieces) == 1135
