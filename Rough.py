# Define the function
def equilibriumPoint(A, N):
    res1 = 0
    res2 = 0
    R = N // 2
    for i in range(R):
        res1 += A[i]

    for j in range(R + 1, N):
        res2 += A[j]

    while res1==res2:
        if res1 == res2:
            return R + 1
        elif res1 > res2:
            R = R - 1
            if R >= 0:
                res2 += A[R + 1]
                res1 -= A[R]
        elif res2 > res1:
            R = R + 1
            if R < N:
                res1 += A[R - 1]
                res2 -= A[R]

    return -1


# Test the function with the provided input
input_list = [30, 20, 17, 42, 25, 32, 32, 30, 32, 37, 9, 2, 33, 31, 17, 14, 40, 9, 12, 36, 21, 8, 33, 6, 6, 10, 37, 12,
              26, 21, 3]
result = equilibriumPoint(input_list, len(input_list))

# Check the result
if result == 13:
    print("The function returned the expected output of 13.")
else:
    print(f"The function returned {result}, but the expected output was 13.")