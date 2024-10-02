import sys
input = sys.stdin.readline
N = int(input())
nums = {}
for _ in range(N):
    num = int(input())
    if num in nums:
        nums[num] += 1
    else:
        nums[num] = 1
freq = max(nums.values())
f = []
for i,k in nums.items():
    if k == freq:
        f.append(i)
f.sort()
print(f[0])