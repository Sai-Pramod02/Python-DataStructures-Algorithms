def firstOcc(arr, x, n):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            if mid == 0 or arr[mid - 1] != arr[mid]:
                return mid
            else:
                high = mid - 1
    return -1


def lastOcc(arr, x, n):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            if mid == (n - 1) or arr[mid] != arr[mid + 1]:
                return mid
            else:
                low = mid + 1
    return -1


def binarysearch(arr, x, n):
    first = firstOcc(arr, x, n)
    if first == -1:
        return 0
    else:
        return lastOcc(arr, x, n) - first + 1


print(binarysearch([1, 2, 3, 4, 5, 5, 5, 6, 7], 5, 9))
