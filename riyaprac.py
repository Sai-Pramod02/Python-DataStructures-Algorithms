t = int(input())
for i in range(t):
    n = int(input())
    s = int(input())
    a = list(map(int, input().split()))
    count = 0;
    for i in range(n):
        for j in range(0,n):
            count = j
            if a[i] == s:
                print(i)
            elif a[i] + a[i+1]*count:
                print()


