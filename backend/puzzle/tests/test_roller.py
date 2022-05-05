import pytest
from src.roller import *


# test roller function
def test_if_get_all_pieces():
    name = 'JS_logo'
    ls = []
    for i in range(100):
        url = roll(name)
        ls.append(url)
        print(url)
    assert len(ls) == 25
