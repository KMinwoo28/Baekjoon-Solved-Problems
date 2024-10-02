import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    rec = list(map(str,input().rstrip().split()))
    meows = {}
    while True:
        op = input().rstrip()
        if op == 'what does the fox say?':
            break
        else:
            sp = list(map(str,op.split()))
            meows[sp[-1]] = 0
    for r in rec:
        if r not in meows:
            print(r, end = ' ')