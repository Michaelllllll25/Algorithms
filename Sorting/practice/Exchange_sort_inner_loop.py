my_list = [45, 87, 39, 32, 93, 86, 12, 44, 75, 50]

# Display the original (unsorted values)
print("before: ", end="")
for n in my_list:
    print(f"{n} ", end="")
print()

# Exchange sort inner loop here...
"""
marker = 0
for ...  # start from marker + 1
    if marker value is greater...
        # swap the values in the two slots
"""
indexing_length = len(my_list) - 1     # ----
sorted = False     # ----

while not sorted:     # ----
    sorted = True     # ----
    for i in range(0, indexing_length):     # ----
        if my_list[i] > my_list[i+1]:    # ----
            sorted = False
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]  # ----

# Display the values again, now after ONE PASS of the exchange sort algorithm.
print("after : ", end="")
for n in my_list:
    print(f"{n} ", end="")
print()
