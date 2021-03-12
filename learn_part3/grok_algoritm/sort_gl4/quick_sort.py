def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pupo = array[0]
        ligth = [i for i in array[1:] if i <= pupo]
        higth = [i for i in array[1:] if i > pupo]
        return quick_sort(ligth) + [pupo] + quick_sort(higth)
arr = [-22, 1, 46, -2, 57843, 0]
print(quick_sort(arr))