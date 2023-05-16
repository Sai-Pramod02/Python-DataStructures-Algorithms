def bubblesort(arr,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


def optimized(arr,n):
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        if swapped == False:
            break
    return arr

print(bubblesort([16,15,14,13,12],5))
print(optimized([16,15,14,13,12],5))
