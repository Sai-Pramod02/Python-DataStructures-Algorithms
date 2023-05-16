def sum_value(arr,sum,n):
    """This function returns a pair of numbers in the given array that are equal to the required sum; Returns -1 if there is o such pair"""

    low=0
    high=n-1
    while low<=high:
        if arr[low]+arr[high]==sum:
            return arr[low],arr[high]
        elif arr[low]+arr[high] >sum:
            high-=1
        else:
            low+=1
    return -1

print(sum_value([2,4,8,9,11,12,20,30],23,8))