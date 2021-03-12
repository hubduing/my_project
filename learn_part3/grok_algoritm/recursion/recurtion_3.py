def sun(arr):
    if arr == []:
        pass
    else:
        print(arr[0] + sun(arr[1:]))

sun([1, 2, 3, 4])