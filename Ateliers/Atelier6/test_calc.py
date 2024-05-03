from unittest import TestCase
import pytest
from calc import multiply

def test_positif():
    assert multiply(5,10) == 50

#Error
def test_positifShouldReturnError():
    assert multiply(5,10) == 51

def test_negatif():
    assert multiply(-5,10) == -50

#Error
def test_negatifShouldReturnError():
    assert multiply(5,10) == 50

def test_zero():
    assert multiply(0,10) == 0

#Error
def test_negatifShouldReturnError():
    assert multiply(0,10) == 50


def test_multiply_with_two_none():
    with pytest.raises(TypeError):
        multiply(None,None)