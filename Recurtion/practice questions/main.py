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
