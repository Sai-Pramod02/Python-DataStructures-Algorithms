def allocation_ispossible(arr, barrier, k):
    allocated_stu = 1
    pages = 0
    for i in range(len(arr)):
        if arr[i] > barrier:
            return False
        elif pages + arr[i] > barrier:
            allocated_stu += 1
            pages += arr[i]
        else:
            pages += arr[i]
    if (allocated_stu > k):
        return False
    return True


def minumumpages(arr, k):
    low = min(arr)
    high = sum(arr)

    while low <= high:
        barrier = (low + high) // 2
        if allocation_ispossible(arr, barrier, k):
            high = barrier - 1
        else:
            low = barrier + 1
    return low


print(minumumpages([5, 7, 100, 11], 4))
