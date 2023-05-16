def inersection(arr1,arr2,m,n):
    i,j=0,0
    temp1=[]
    while i<m and j<n:
        if i>0 and arr1[i]==arr1[i-1]:
            i+=1
            continue
        if j>0 and arr2[j]==arr2[j-1]:
            j+=1
            continue
        if arr1[i]<arr2[j]:
            i+=1
        elif arr1[i]>arr2[j]:
            j+=1
        else:
            temp1.append(arr1[i])
            i+=1
            j+=1
    return temp1
def union(arr1,arr2,m,n):
    i,j=0,0
    temp=[]
    while i<m and j<n:
        if i>0 and arr1[i]==arr1[i-1]:
            i+=1
            continue
        if j>0 and arr2[j]==arr2[j-1]:
            j+=1
            continue
        if arr1[i]<=arr1[j]:
            temp.append(arr1[i])
            i+=1
        else:
            temp.append(arr2[j])
            j+=1
    while i<m:
        temp.append(arr1[i])
        i+=1
    while j<n:
        temp.append(arr2[j])
        j+=1
    return temp

print(inersection([2,10,20,20,40],[3,20,40],5,3))
print(union([2,10,20,20],[3,20,40],4,3))
