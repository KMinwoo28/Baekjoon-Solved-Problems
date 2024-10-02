import sys
input = sys.stdin.readline
N = int(input())
dic = {}
for _ in range(N):
    book = input().rstrip()
    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1
max_sell = max(dic.values())
bestsell = []
for b,i in dic.items():
    if i == max_sell:
        bestsell.append(b)
bestsell.sort()
print(bestsell[0])