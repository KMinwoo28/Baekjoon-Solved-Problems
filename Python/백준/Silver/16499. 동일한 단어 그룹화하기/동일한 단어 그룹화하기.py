import sys
input = sys.stdin.readline
N = int(input())
lst = {}
for _ in range(N):
    word = list(input().rstrip())
    word.sort()
    if ''.join(word) not in lst:
        lst[''.join(word)] = 1
print(len(lst))