import pytest
import sys
  
sys.path.insert(0, '/src/puzzle/')
from puzzle import *

# test number of puzzle
def test_number_of_pieces():
    url = 'https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/python.png?raw=true'
    p = Puzzle(url, 30, 'test')
    assert len(p.pieces) == 1135
