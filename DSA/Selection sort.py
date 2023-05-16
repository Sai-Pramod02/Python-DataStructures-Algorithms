def selection_sort(arr,n):
    for i in range(n-1):
        min_index = i
        for j in range(min_index+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([15,14,13,12,11],5))
