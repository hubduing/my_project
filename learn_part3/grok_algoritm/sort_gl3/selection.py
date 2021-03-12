def ind_smallest(arr):
    smallest = arr[0]
    smallest_ind = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_ind = i
            smallest = arr[i]
    return smallest_ind

def selection(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = ind_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr
arr = [2, 1, 3, 7, 4, 6, 9]
print(selection(arr))