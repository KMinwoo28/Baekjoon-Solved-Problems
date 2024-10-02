def maxnum(a):
    maxone = 0
    for i in range(3):
        for j in range(i+1,4):
            for k in range(j+1,5):
                if maxone < (a[i]+a[j]+a[k]) % 10:
                    maxone = (a[i]+a[j]+a[k]) % 10
    return maxone

N = int(input())
res = {}
for i in range(1, N+1):
    sc = list(map(int,input().split()))
    res[i] = maxnum(sc)
result = sorted(res.items(), key = lambda x:(-x[1],-x[0]))
print(result[0][0])