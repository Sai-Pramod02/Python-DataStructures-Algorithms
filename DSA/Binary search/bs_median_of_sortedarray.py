def median(arr1,arr2):
    A,B= arr1,arr2
    total = len(A) + len(B)
    half = total//2  #Tells us the total elements in the left partition
    if len(A)>len(B):
        A,B = B,A

    l=0
    r=len(A)-1
    while True:
        i=(l+r)//2 #A
        j = half-i-2  #B

        Aleft = A[i] if i>=0 else float ("-infinity")
        Aright = A[i+1] if i+1<len(A) else float ("infinity")
        Bleft = B[j] if j>=0 else float ("-infinity")
        Bright = B[j+1] if j+1<len(B) else float("infinity")

        if Aleft<=Bright and Bleft<=Aright:
            #Odd
            if total%2:
                return min(Aright,Bright)
            else:
                return (max(Aleft, Bleft) + min(Aright,Bright))//2
        elif Aleft>Bright:
            r=i-1
        else:
            l=i+1

print(median([1,2,3,4,5],[1,2,3,4,5,6,7,8]))

