n = int(input())
res = 0
while True:
    if n % 5 == 0:
        res += n// 5
        break
    else:
        n -= 2
        res += 1
    if n < 0:
        break
if n < 0:
    print(-1)
else:
    print(res)