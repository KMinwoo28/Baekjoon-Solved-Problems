import sys
input = sys.stdin.readline
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()
print(round(sum(nums)/N))
print(nums[N//2])
freq = {}
for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1
max_freq = max(freq.values())
mf = []
for n in freq:
    if max_freq == freq[n]:
        mf.append(n)
if len(mf) > 1:
    print(mf[1])
else:
    print(mf[0])

print(nums[-1] - nums[0])