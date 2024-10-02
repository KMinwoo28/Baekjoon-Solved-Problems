import sys
input = sys.stdin.readline
N = int(input())
numlist = list(map(int,input().split()))
numlist.sort()
count = 0
for target in numlist:
    test = numlist[:]
    test.remove(target)
    left, right= 0, N - 2
    while(left<right):
        if test[left] + test[right] == target:
            count += 1
            break
        if test[left] + test[right] <target:
            left += 1
            continue
        right -= 1
print(count)  