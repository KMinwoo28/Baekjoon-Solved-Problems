n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
nums.sort()
for j in range(n):
    print(nums[j])