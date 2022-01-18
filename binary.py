list = [5, 7, 8, 10, 11, 14, 22]
left = list[0]
right = list[6]
target = 7
while right >= left:
    mid = (left + right)//2
    print(mid)
    #Found
    if list[mid] == target:
        print(mid) 
    elif target < list[mid]:
        right = mid - 1
    elif target > list[mid]:
        left = mid + 1
