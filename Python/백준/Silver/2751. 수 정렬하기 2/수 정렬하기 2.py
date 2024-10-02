import sys
n = int(sys.stdin.readline())
numlist = list()
for _ in range(n):
    numlist.append(int(sys.stdin.readline()))
numlist.sort()
for num in numlist:
    print(num)