def lastOcc(arr, x, n):
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high) // 2
        if (arr[mid] > x):
            high = mid - 1
        elif (arr[mid] < x):
            low = mid + 1
        else:
            if mid == (n - 1) or arr[mid] != arr[mid + 1]:
                return mid
            else:
                low = mid + 1
    return -1

print(lastOcc([1, 2, 2, 3, 4, 5, 5, 6], 5, 8))
