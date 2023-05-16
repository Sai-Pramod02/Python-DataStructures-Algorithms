def repeating(arr):
    visited=[]
    for i in range(len(arr)-1):
        visited.append(False)
    for j in range (len(arr)):
        if visited[arr[j]]:
            return arr[j]
        visited[arr[j]]=True

def repeating_efficient(arr):
    slow=arr[0]
    fast=arr[0]
    while slow!=fast:
        slow=arr[slow]
        fast=arr[arr[fast]]
    return arr[slow]
def repeating_efficient1(arr):
    slow=arr[0]
    fast=arr[len(arr)-1]
    while slow!=fast:
        slow=arr[slow]
        fast=arr[fast]
        return slow
print(repeating([0,1,2,3,4,4,5]))
print(repeating_efficient([1,2,3,4,4,5]))
print(repeating_efficient1([1,2,3,4,4,5]))
