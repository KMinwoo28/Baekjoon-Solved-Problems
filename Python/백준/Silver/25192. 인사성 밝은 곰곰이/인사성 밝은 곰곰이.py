import sys
input = sys.stdin.readline
log = {}
count = 0
N = int(input())
for _ in range(N):
    op = input().rstrip()
    if op == 'ENTER':
        log.clear()
    else:
        if op not in log:
            count += 1
            log[op] = 0
print(count) 