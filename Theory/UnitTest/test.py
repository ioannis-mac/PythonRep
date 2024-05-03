
from unittest import TestCase

import pytest
from main import add

#def add(a,b):
#    return a+b

class TestCalculatrice(TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add(5,10),15)

