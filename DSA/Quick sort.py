def partitionIndex(arr,low,high):
    pivot = arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
    return j

def quickSort(arr,low,high):
    if low<=high:
        pIndex = partitionIndex(arr,low,high)
        quickSort(arr,low,pIndex-1)
        quickSort(arr,pIndex+1,high)
    return arr

def Question(arr):

    quickSort(arr,0,len(arr)-1)
    return arr

print(Question([4,6,2,5,7,9,1,3]))
