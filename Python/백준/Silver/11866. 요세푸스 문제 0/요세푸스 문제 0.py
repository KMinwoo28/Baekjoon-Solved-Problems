n, k = map(int,input().split())
loc = 0
remain = [i for i in range(1,n+1)]
res = []
while remain:
    loc += k - 1
    if loc >= len(remain):
        loc %= len(remain)
    res.append(str(remain.pop(loc)))
print("<",", ".join(res), ">", sep = "")