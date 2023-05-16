def insertion_sort(arr,n):
    for i in range(n-1):
        key = arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(insertion_sort([20,5,40,60,10,30],6))