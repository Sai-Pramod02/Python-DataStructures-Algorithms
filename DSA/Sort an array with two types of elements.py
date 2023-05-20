#Quick sort works as the most efficient algorithm for all these type of problems
def pstngt(arr,low,high):
    '''
    function for segregating positive and negatives
    '''
    i = low
    j = high
    pivot = arr[low]
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
def qsPstNgt(arr,low,high):
    if low<=high:
        p=pstngt(arr,low,high)
        qsPstNgt(arr,low,p-1)
        qsPstNgt(arr,p+1,high)
        return arr

def oddEven(arr,low,high):
    '''
    function for segregating odd and even numbers
    '''
    i = low
    j = high
    pivot = arr[low]
    while i<j:
        while  arr[i]%2==0 and i<=high-1:
            i+=1
        while  arr[j]%2!=0 and j>=low+1:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
def qsOddEven(arr,low,high):
    if low<=high:
        p=oddEven(arr,low,high)
        qsOddEven(arr,low,p-1)
        qsOddEven(arr,p+1,high)
        return arr

def Binary(arr,low,high):
    '''
    function for segreating zero's and one's
    '''
    i = low
    j = high
    pivot = arr[low]
    while i<j:
        while  arr[i]==0 and i<=high-1:
            i+=1
        while  arr[j]==1 and j>=low+1:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
def qsBinary(arr,low,high):
    if low<=high:
        p=Binary(arr,low,high)
        qsBinary(arr,low,p-1)
        qsBinary(arr,p+1,high)
        return arr



print("Segreating positive and negative numbers : ",qsPstNgt([-12,18,-10,15],0,3))
print("Segregating even and odd numbers : ",qsOddEven([15,14,13,12],0,3))
print("Segregating 0's and 1's : ",qsBinary([0,1,1,1,0],0,4))
