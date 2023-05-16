def srtdrotd(arr, x, n):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] >= arr[low]:
            if arr[low]<=x<arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        elif arr[mid] <= arr[low]:
            if arr[high]>=x>arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


print(srtdrotd([100, 200, 300, 400, 20, 30, 40], 40, 7))
