import pytest
from main import add

def test_add_with_two_number():
    assert add(5,10) == 15

#Error
def test_add_with_two_numberShouldReturnError():
    assert add(5,10) == 10

def test_add_with_two_letters():
    assert add("a", "b") == "ab"

#Error
def test_add_with_two_lettersShouldReturnError():
    assert add("a", "") == "ab"

def test_add_with_two_booleans():
    assert add(True, False) == 1
    assert add(True, True) == 2
    assert add(False, False) == 0

def test_add_with_two_booleansShouldReturnError():
    assert add(True, True) == 1

def test_add_with_two_none():
    with pytest.raises(TypeError):
        add(None,None)