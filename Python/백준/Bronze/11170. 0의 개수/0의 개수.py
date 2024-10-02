T = int(input())
for i in range(T):
    m, n = map(int, input().split())
    result = ''.join(str(j) for j in range(m, n+1))
    print(result.count('0'))