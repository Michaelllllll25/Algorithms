from main import factorial
from main import bunny_ears



def test_factorial_1():
    assert factorial(1) == 1


def test_factorial_2():
    assert factorial(2) == 2


def test_factorial_3():
    assert factorial(3) == 6


def test_factorial_4():
    assert factorial(4) == 24


def test_factorial_5():
    assert factorial(5) == 120


def test_factorial_6():
    assert factorial(6) == 720


def test_factorial_7():
    assert factorial(7) == 5040


def test_factorial_8():
    assert factorial(8) == 40320


def test_factorial_9():
    assert factorial(12) == 479001600

# ------------------------------------------

def test_bunny_ears_1():
    assert bunny_ears(0) == 0


def test_bunny_ears_2():
    assert bunny_ears(1) == 2


def test_bunny_ears_3():
    assert bunny_ears(2) == 4


def test_bunny_ears_4():
    assert bunny_ears(3) == 6


def test_bunny_ears_5():
    assert bunny_ears(4) == 8


def test_bunny_ears_6():
    assert bunny_ears(5) == 10


def test_bunny_ears_7():
    assert bunny_ears(12) == 24


def test_bunny_ears_8():
    assert bunny_ears(50) == 100


def test_bunny_ears_9():
    assert bunny_ears(234) == 468
