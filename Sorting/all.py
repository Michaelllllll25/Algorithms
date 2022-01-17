# This simple sorting algorithm iterates over a list, comparing elements in pairs and swapping them until the larger elements 
# "bubble up" to the end of the list, and the smaller elements stay at the "bottom".

def bubble_sort(nums):
    # We swap to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # set the flag to True so it will loop again
                swapped = True

nums = [5, 2, 1, 8, 4]
bubble_sort(nums)
print(nums)


# This algorithm segments the list into two parts: sorted and unsorted. We continuously remove the smallest element of the unsorted 
# segment of the list and append it to the sorted segment.

def selection_sort(random_list_of_nums):
    # This value of i corresponds to how many values were sorted
    for i in range(len(random_list_of_nums)):
        # We assume that the first item of the unsorted list is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(random_list_of_nums)):
            if random_list_of_nums[j] < random_list_of_nums[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted element
        random_list_of_nums[i], random_list_of_nums[lowest_value_index] = random_list_of_nums[lowest_value_index], random_list_of_nums[i]

random_list_of_nums = [12, 8, 3, 20, 11]
selection_sort(random_list_of_nums)
print(random_list_of_nums)

# Like Selection Sort, this algorithm segments the list into sorted and unsorted parts. It iterates over the unsorted segment, 
# and inserts the element being viewed into the correct position of the sorted list.

def insert_sort(list_of_nums):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(list_of_nums)):
        item_to_insert = list_of_nums[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than the item to insert
        while j >= 0 and list_of_nums[j] > item_to_insert:
            list_of_nums[j + 1] = list_of_nums[j]
            j -= 1
        # Insert the item
        list_of_nums[j + 1] = item_to_insert

list_of_nums = [9, 1, 15, 28, 6]
insert_sort(list_of_nums)
print(list_of_nums)            

# This popular sorting algorithm, like the Insertion and Selection sorts, segments the list into sorted and unsorted parts. 
# It converts the unsorted segment of the list to a Heap data structure, so that we can efficiently determine the largest element.   
def heapify(heap_nums, heap_size, root_index):
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    if left_child < heap_size and heap_nums[left_child] > heap_nums[largest]:
        largest = left_child

    # Do the same for the right child of the root
    if right_child < heap_size and heap_nums[right_child] > heap_nums[largest]:
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        heap_nums[root_index], heap_nums[largest] = heap_nums[largest], heap_nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(heap_nums, heap_size, largest)


def heap_sort(heap_nums):
    n = len(heap_nums)

    # Create a Max Heap from the list
    # The 2nd argument of range means we stop at the element before -1 i.e.
    # the first element of the list.
    # The 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    for i in range(n, -1, -1):
        heapify(heap_nums, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        heap_nums[i], heap_nums[0] = heap_nums[0], heap_nums[i]
        heapify(heap_nums, i, 0)


# Verify it works
heap_nums = [35, 12, 43, 8, 51]
heap_sort(heap_nums)
print(heap_nums)


# This divide and conquer algorithm splits a list in half, and keeps splitting the list by 2 until it only has singular elements.

# Adjacent elements become sorted pairs, then sorted pairs are merged and sorted with other pairs as well. 
# This process continues until we get a sorted list with all the elements of the unsorted input list.

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # We use the list lengths often, so its handy to make variables
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it
            # to the sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # If we've reached the end of the of the left list, add the elements
        # from the right list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # If we've reached the end of the of the right list, add the elements
        # from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(merge_nums):
    # If the list is a single element, return it
    if len(merge_nums) <= 1:
        return merge_nums

    # Use floor division to get midpoint, indices must be integers
    mid = len(merge_nums) // 2

    # Sort and merge each half
    left_list = merge_sort(merge_nums[:mid])
    right_list = merge_sort(merge_nums[mid:])

    # Merge the sorted lists into a new one
    return merge(left_list, right_list)


# Verify it works
merge_nums = [120, 45, 68, 250, 176]
merge_nums = merge_sort(merge_nums)
print(merge_nums)
