''' My Calculator Test'''
from calculator import add, subtract

def test_addition():
    ''' Testing addition function'''
    assert add(2, 2) == 4

def test_subtraction():
    ''' Testing the subtraction function'''
    assert subtract(2, 2) == 0
