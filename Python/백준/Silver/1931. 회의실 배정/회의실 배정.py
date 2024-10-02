import sys
input = sys.stdin.readline
n = int(input())
end = 0
res = 0
time = []
for _ in range(n):
    a, b = map(int,input().split())
    time.append([a,b])
time.sort(key = lambda x:(x[1],x[0])) # 빨리 끝나고, 빨리 시작하는 순서로 정렬
for st, ed in time:
    if st >= end:
        res += 1
        end = ed
print(res)