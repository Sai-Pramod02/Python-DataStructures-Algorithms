def bs(arr,n):
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==0:
            low=mid+1
        else:
            if mid==0 or arr[mid-1]==0:
                return (n)-mid
            else:
                high=mid-1
    return 0

print(bs([0,0,1,1,1,1,1],7))