def two_pointer(arr,sum,startingindex,n):
    low=startingindex
    high=n-1
    while low<=high:
        if(arr[low]+arr[high]==sum):
            return True
        elif arr[low]+arr[high]>sum:
            high-=1
        else:
            low+=1
    return False
def triplets(arr,sum,n):
    """This functions returns a pair of triplets whose sum is equal to the required sum;
    It uses an approach of first considering a number in an array and then checking
    for a pair of other two numbers in the array whose sum is equal to the required sum minus the number considered initially
    Example:-
    [2,3,4,8,9,20,40]   required sum is 32
    consider 2 first: 32-2=30
    check for a pair of two numbers from 3 to 40 whose sum is 30 using two pointers approach
    """
    for i in range(0,n-2):
        if two_pointer(arr, sum - arr[i], i + 1,n):
            return True

    return False

print(triplets([2,3,4,8,9,20,40],32,7))


