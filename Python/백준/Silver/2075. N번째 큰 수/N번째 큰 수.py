import sys
input = sys.stdin.readline
import heapq
N = int(input())
Array = []
for _ in range(N):
    nums = list(map(int,input().split()))
    if not Array:               # 최초 N개 배열을 heap에 저장
        for num in nums:
            heapq.heappush(Array,num)
    else:                       # 이후 N개 유지
        for num in nums:
            if num > Array[0]:   #들어오는 값이 배열 최소보다 크다면:
                heapq.heappush(Array,num)
                heapq.heappop(Array)    #최소값과 교체
print(Array[0]) 