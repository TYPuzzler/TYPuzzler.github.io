import pytest
from src.puzzle import *


# test number of puzzle
def test_number_of_pieces():
    url = 'https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/Python_(programming_language).png?raw=true'
    p = Puzzle(url, 30, 'test')
    assert len(p.pieces) == 1135
