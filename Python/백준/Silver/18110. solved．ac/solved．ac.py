# 사사오입 반올림 적용해야함
def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)
import sys
input = sys.stdin.readline
n = int(input())
if n == 0:
    print(0)
    sys.exit()
rate = []
for _ in range(n):
    rate.append(int(input()))
rate.sort()
truc = round2(n*0.15)
target = rate[truc:n-truc]
print(round2(sum(target)/len(target))) # Average