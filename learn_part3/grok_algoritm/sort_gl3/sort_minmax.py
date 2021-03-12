def sort(arr):
    smallest = arr[0]
    smallest_ind = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_ind = i
            smallest = arr[i]
    return smallest_ind
arr = [4, 3, 1, 7, 9, 6, 5]
print(sort(arr))