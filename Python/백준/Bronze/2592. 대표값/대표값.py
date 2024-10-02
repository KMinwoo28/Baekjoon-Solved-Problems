nums = []
for _ in range(10):
    nums.append(int(input()))
print(sum(nums)//10)
maxfreq = 0
for i in range(10):
    if maxfreq < nums.count(nums[i]):
        maxfreq = i
print(nums[maxfreq])