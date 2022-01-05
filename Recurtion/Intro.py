# Recursion
# - functions calling themselves

# def hello():
#     hello()   # recursion
# hello()

# Stack Overflow (Infinite recursion)


def count_to(n: int):
    if n == 0:         # base case
        print(n)
        return
    count_to(n-1)
    print(n)

count_to(2)

# ------------------

def sum_to(n: int):
    if n == 1:
        return 1
    return n + sum_to(n-1)

print(sum_to(3))

# ---------------------

def even_nums(num):
    print(num)
    if num % 2 != 0:
        print("Please enter even number")
    if num == 2:
        return num 
    else:
        return even_nums(num-2)

even_nums(8)

# -----------------------------------

# COUNT TO 5
# Loop version

for n in range(6):
    print(n)


print()

# recursion
def count_to(n: int) -> None:
    if n == 0:
        print(n)
        return
    count_to(n - 1)  # recursive step
    print(n)


count_to(5)

print()
# SUMMATION OF A RANGE
# with a loop

total = 0
for n in range(6):
    total += n

print(total)


# with recursion
def sum_to(n: int) -> int:
    if n == 0:
        return 0
    
    return n + sum_to(n-1)

print(sum_to(5))
