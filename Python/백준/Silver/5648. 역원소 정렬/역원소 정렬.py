import sys
input = sys.stdin.readline
first = list(input().split())
n = int(first[0])
nums = [int(first[i][::-1]) for i in range(1,len(first))]
while len(nums) < n:
    rec = list(input().split())
    for i in range(len(rec)):
        nums.append(int(rec[i][::-1]))
nums.sort()
for n in nums:
    print(n)