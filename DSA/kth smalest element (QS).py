#Finding the Kth smallest element in ar array which also consists of duplicates
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


def qs(arr,low,high,k):
    while low<=high:
        p = partitionIndex(arr,low,high)
        qs(arr,low,p-1,k)
        qs(arr,p+1,high,k)
        if p==k-1:
            if arr[p-1]!=arr[p]:
                return arr[p]
            else:
                return arr[p+1]
        elif p>(k-1):
            high=p-1
        else:
            low=p+1

print("Optimal Method : ",qs([5,2,2,1,4,3],0,5,3))

