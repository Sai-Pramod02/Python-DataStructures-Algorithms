#Using binary search we find out the peak element
# The concept is that, if the element to the left of mid is greater than mid then there would definitely be a peak element.
#Therefore, we compare the mid-value with the left and right values and perform binary search
#Note that the first and last elements are to be compared with their one and only one neighbour values
def peak_element(arr,n):
    low=1
    high=n-2
    if arr[0] > arr[1]:
        return arr[0]
    if arr[n - 1] > arr[n - 2]:
        return arr[n - 1]
    while low<=high:
        mid = (low+high)//2
        if arr[mid-1]>arr[mid]:
            high=mid-1
        elif arr[mid+1]>arr[mid]:
            low=mid+1
        else:
            return arr[mid]
    return -1

print(peak_element([5,20,40,30,20,50,20],7))
