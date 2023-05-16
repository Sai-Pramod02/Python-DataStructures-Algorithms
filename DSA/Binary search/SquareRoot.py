def naive(x):
    i = 1
    while (i * i <= x):
        i += 1
    return i - 1


print(naive(16))


def bs_sqrt(x):
    low = 1
    high = x
    while low <= high:
        mid = (low + high) // 2
        if mid * mid > x:
            high = mid - 1
        elif mid * mid < x:
            low = mid + 1
            ans = mid
        else:
            return mid
    return ans


print(bs_sqrt(39))
