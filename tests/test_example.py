# you can import your modules and test them here
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4]

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 2 - 1 == 1

def test_sum(sample_data):
    assert sum(sample_data) == 10

class TestMathOperations:
    def test_multiplication(self):
        assert 2 * 2 == 4

    def test_division(self):
        assert 4 / 2 == 2
