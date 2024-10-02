N = int(input())
res = 1
for i in range(1,N+1):
    res *= i
res = str(res)
zero = 0
for k in range(1,len(res)+1):
    if res[-k] == '0':
        zero += 1
    else:
        break
print(zero)