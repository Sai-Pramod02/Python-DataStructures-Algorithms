def median(arr1,arr2,n):
    A,B = arr1, arr2
    if(len(B)>len(A)):
        A,B = B,A
    total = len(A)+len(B)
    half = total//2
    l=0
    r=len(A)-1
    while True:
        i = (l+r)//2
        j = half-i-2

        Aleft = A[i] if i>=0 else float("-infinity")
        Aright = A[i+1] if i+1<len(A) else float("infinity")


        if Aleft<=Bright and Bleft<=Aright:
            if total%2:
                return min(Bleft,Bright)
            else:
                return min