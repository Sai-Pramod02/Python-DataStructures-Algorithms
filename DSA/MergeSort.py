def Merge(arr,low,mid,high):
    temp=[]
    left = low
    right = mid+1
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]
    return arr

def Ms(arr,low,high):
    if low==high:
        return
    mid=(low+high)//2
    Ms(arr,low,mid)
    Ms(arr,mid+1,high)
    Merge(arr,low,mid,high)
    return arr


print(Ms([3,1,2,4,1,5,6,2,4],0,8))