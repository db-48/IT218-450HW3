''' My Calculator Test'''
from calculator import Calculator

def test_addition():
    ''' Testing addition function'''
    assert Calculator.add(2, 2) == 4

def test_subtraction():
    ''' Testing the subtraction function'''
    assert Calculator.subtract(2, 2) == 0

def test_multiply():
    ''' Testing the multiplication function'''
    assert Calculator.multiply(2, 2) == 4

def test_divide():
    ''' Testing the divison function'''
    assert Calculator.divide(2, 2) == 1
    