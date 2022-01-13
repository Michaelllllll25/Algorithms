def factorial(n: int) -> int:
    if n == 0:       # base case
        return 1
    else:                                # recursion step
        return n * factorial(n-1)


result = factorial(1)
print(result)

# ----------------------------------------

def bunny_ears(bunnies: int) -> int:
    if bunnies == 0:
        return 0 
    else:
        return 2 + bunny_ears(bunnies-1)


result = bunny_ears(2)
print(result)

def fibonacci(n: int) -> int:
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n -2)


result = fibonacci(0)
print(result)

def bunny_ears_2(bunnies: int) -> int:
    if bunnies == 0:
        return 0

    if bunnies % 2 == 1:
        return 2 + bunny_ears_2(bunnies - 1)

    return 3 + bunny_ears_2(bunnies - 1)

result = bunny_ears_2(0)
print(result)

def triangle(rows: int) -> int:
    if rows == 0:
        return 0

    return rows + triangle(rows - 1)

result = triangle(0)
print(result)

def sum_digits(n: int) -> int:
    if n == 0:
        return 0
    
    return n % 10 + sum_digits(n // 10)

result = sum_digits(126)
print(result)

def count_7(n: int) -> int:
    if n == 0:
        return 0
    
    if n % 10 == 7:
        return 1 + count_7(n // 10)

    return count_7(n // 10)
    
result = count_7(717)
print(result)

def count_8(n: int) -> int:
    if n == 0: 
        return 0

    if n % 10 == 8:
        if n // 10 % 10 == 8:
            return 2 + count_8(n // 10)
        return 1 + count_8(n // 10)
    
    return count_8(n // 10)

result = count_8(8)
print(result)

def power_n(base: int, n: int) -> int:
    if n <= 1:
        return base
    
    return base * power_n(base, n - 1)

result = power_n(3, 1)
print(result)

def count_x(string: str) -> int:
    pass

result = count_x('xxhixx')
print(result)

def count_hi(string: str) -> int:
    if string == "":
        return 0

    first_two = string[:2]
    if first_two == "hi":
        remaining = string[2:]
        return 1 + count_hi(remaining)

    remaining = string[1:]
    return 0 + count_hi(remaining)

result = count_hi('xxhixx')
print(result)


https://github.com/mirandaio/codingbat/blob/master/java/recursion-1/changeXY.java

