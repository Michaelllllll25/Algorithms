from main import factorial
from main import bunny_ears
from new import fibonacci
from new import bunny_ears_2
from new import triangle
from new import sum_digits
from new import count_7
from new import count_8
from new import power_n
from new import count_x
from new import count_hi


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
# --------------------------------------
def test_fibonacci_1():
    assert fibonacci(0) == 0


def test_fibonacci_2():
    assert fibonacci(1) == 1


def test_fibonacci_3():
    assert fibonacci(2) == 1


def test_fibonacci_4():
    assert fibonacci(3) == 2


def test_fibonacci_5():
    assert fibonacci(4) == 3


def test_fibonacci_6():
    assert fibonacci(5) == 5


def test_fibonacci_7():
    assert fibonacci(6) == 8


def test_fibonacci_8():
    assert fibonacci(7) == 13

# -----------------

def test_bunny_ears_2_1():
    assert bunny_ears_2(0) == 0


def test_bunny_ears_2_2():
    assert bunny_ears_2(1) == 2


def test_bunny_ears_2_3():
    assert bunny_ears_2(2) == 5


def test_bunny_ears_2_4():
    assert bunny_ears_2(3) == 7


def test_bunny_ears_2_5():
    assert bunny_ears_2(4) == 10


def test_bunny_ears_2_6():
    assert bunny_ears_2(5) == 12


def test_bunny_ears_2_7():
    assert bunny_ears_2(6) == 15


def test_bunny_ears_2_8():
    assert bunny_ears_2(10) == 25

# -----------------

def test_triangle_1():
    assert triangle(0) == 0


def test_triangle_2():
    assert triangle(1) == 1


def test_triangle_3():
    assert triangle(2) == 3


def test_triangle_4():
    assert triangle(3) == 6


def test_triangle_5():
    assert triangle(4) == 10


def test_triangle_6():
    assert triangle(5) == 15


def test_triangle_7():
    assert triangle(6) == 21


def test_triangle_8():
    assert triangle(7) == 28
# -----------------
def test_sum_digits_1():
    assert sum_digits(126) == 9


def test_sum_digits_2():
    assert sum_digits(49) == 13


def test_sum_digits_3():
    assert sum_digits(12) == 3


def test_sum_digits_4():
    assert sum_digits(10) == 1


def test_sum_digits_5():
    assert sum_digits(1) == 1


def test_sum_digits_6():
    assert sum_digits(0) == 0


def test_sum_digits_7():
    assert sum_digits(730) == 10


def test_sum_digits_8():
    assert sum_digits(1111) == 4


def test_sum_digits_9():
    assert sum_digits(11111) == 5


def test_sum_digits_10():
    assert sum_digits(10110) == 3


def test_sum_digits_11():
    assert sum_digits(235) == 10
# -----------------
def test_count_7_1():
    assert count_7(717) == 2


def test_count_7_2():
    assert count_7(7) == 1


def test_count_7_3():
    assert count_7(123) == 0


def test_count_7_4():
    assert count_7(77) == 2


def test_count_7_5():
    assert count_7(7123) == 1


def test_count_7_6():
    assert count_7(771237) == 3


def test_count_7_7():
    assert count_7(771737) == 4


def test_count_7_8():
    assert count_7(47571) == 2


def test_count_7_9():
    assert count_7(777777) == 6


def test_count_7_10():
    assert count_7(70701277) == 4


def test_count_7_11():
    assert count_7(777576197) == 5


def test_count_7_12():
    assert count_7(99999) == 0


def test_count_7_13():
    assert count_7(99799) == 1
# -----------------
def test_count_8_1():
    assert count_8(8) == 1


def test_count_8_2():
    assert count_8(818) == 2


def test_count_8_3():
    assert count_8(8818) == 4


def test_count_8_4():
    assert count_8(8088) == 4


def test_count_8_5():
    assert count_8(123) == 0


def test_count_8_6():
    assert count_8(81238) == 2


def test_count_8_7():
    assert count_8(88788) == 6


def test_count_8_8():
    assert count_8(8234) == 1


def test_count_8_9():
    assert count_8(2348) == 1


def test_count_8_10():
    assert count_8(23884) == 3


def test_count_8_11():
    assert count_8(0) == 0


def test_count_8_12():
    assert count_8(1818188) == 5


def test_count_8_13():
    assert count_8(8818181) == 5


def test_count_8_14():
    assert count_8(1080) == 1


def test_count_8_15():
    assert count_8(188) == 3


def test_count_8_16():
    assert count_8(88888) == 9


def test_count_8_17():
    assert count_8(9898) == 2


def test_count_8_18():
    assert count_8(78) == 1
# -----------------
def test_power_n_1():
    assert power_n(3, 1) == 3


def test_power_n_2():
    assert power_n(3, 2) == 9


def test_power_n_3():
    assert power_n(3, 3) == 27


def test_power_n_4():
    assert power_n(2, 1) == 2


def test_power_n_5():
    assert power_n(2, 2) == 4


def test_power_n_6():
    assert power_n(2, 3) == 8


def test_power_n_7():
    assert power_n(2, 4) == 16


def test_power_n_8():
    assert power_n(2, 5) == 32


def test_power_n_9():
    assert power_n(10, 1) == 10


def test_power_n_10():
    assert power_n(10, 2) == 100


def test_power_n_11():
    assert power_n(10, 3) == 1000
# -----------------
# def test_count_x_1():
#     assert count_x('xxhixx') == 4


# def test_count_x_2():
#     assert count_x('xhixhix') == 3


# def test_count_x_3():
#     assert count_x('hi') == 0


# def test_count_x_4():
#     assert count_x('h') == 0


# def test_count_x_5():
#     assert count_x('x') == 1


# def test_count_x_6():
#     assert count_x('') == 0


# def test_count_x_7():
#     assert count_x('hihi') == 0


# def test_count_x_8():
#     assert count_x('hiAAhi12hi') == 0
# -----------------
def test_count_hi_1():
    assert count_hi('xxhixx') == 1


def test_count_hi_2():
    assert count_hi('xhixhix') == 2


def test_count_hi_3():
    assert count_hi('hi') == 1


def test_count_hi_4():
    assert count_hi('hihih') == 2


def test_count_hi_5():
    assert count_hi('h') == 0


def test_count_hi_6():
    assert count_hi('') == 0


def test_count_hi_7():
    assert count_hi('ihihihihih') == 4


def test_count_hi_8():
    assert count_hi('ihihihihihi') == 5


def test_count_hi_9():
    assert count_hi('hiAAhi12hi') == 3


def test_count_hi_10():
    assert count_hi('xhixhxihihhhih') == 3


def test_count_hi_11():
    assert count_hi('ship') == 1


