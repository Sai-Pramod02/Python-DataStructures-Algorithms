
def merge(arr, low, mid, high):
    left = low
    right = mid + 1
    temp = []
    count=0
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            count += mid-low+1
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(low, high + 1):
        arr[i] = temp[i - low]
    return count
def mergeSort(arr, low, high):
    count=0
    if low == high:
        return count
    mid = (low + high) // 2
    count +=mergeSort(arr, low, mid)
    count += mergeSort(arr, mid + 1, high)
    count += merge(arr, low, mid, high)
    return count

def countInversions(arr):
    return mergeSort(arr,0,len(arr)-1)


print(countInversions([4,3,2,1]))
