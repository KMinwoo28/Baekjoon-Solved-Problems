import heapq
import sys
input = sys.stdin.readline
heap = []
N = int(input())
for _ in range(N):
    op = int(input())
    if op == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)*(-1))
    else:
        heapq.heappush(heap, -op)