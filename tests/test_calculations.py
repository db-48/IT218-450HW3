'''My Calculator Test'''
from calculator.operations import add, multiply, subtract, divide

def test_addition():
    '''Testing the addition function'''    
    assert add(2,2) == 4

def test_subtraction():
    '''Testing the subtraction function  '''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Testing that multiplication function'''
    assert multiply(2,2) == 4

def test_division():
    '''Testing the division function'''
    assert divide(2,2) == 1
    