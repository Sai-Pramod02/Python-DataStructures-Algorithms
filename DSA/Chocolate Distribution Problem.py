'''
step1 : Sort the array
step2 : Find the difference between a particular element and it's (m-1)th element
step3: Return the minimum difference among all such pairs
'''
def chocolate(arr,m):
    arr.sort()
    n = len(arr)
    if m>n:
        return -1
    res = arr[m-1]-arr[0] # Finding the difference between the m-1th element and the first element since it is not done in the loop
    i=1
    while (i+m-1)<n:
        res = min(res,arr[i+m-1]-arr[i])
        i+=1
    return res

print(chocolate([7,3,2,4,9,12,56],3))
