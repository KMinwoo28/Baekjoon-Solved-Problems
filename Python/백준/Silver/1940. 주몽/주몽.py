import sys
input = sys.stdin.readline
N = int(input())
x = int(input())
numlist = list(map(int,input().split()))
numlist.sort()
left, count, right = 0,0,N-1
while left < right:
    if numlist[left] + numlist[right] == x:
        count += 1
    if numlist[left] + numlist[right] < x:
        left += 1
        continue
    right -= 1
print(count)