'''
Step1 - Sort the array
step2 - Find the minimum difference between adjacent elements (Assign result to infinity so that it returns the minimum difference
step3 - Return the miniumum difference
'''

def minDiff(arr):
    arr.sort()
    n=len(arr)
    res=float('inf')
    for i in range(1,n):
        res = min(res,(arr[i]-arr[i-1]))
    return res
print(minDiff([10,8,1,4]))

