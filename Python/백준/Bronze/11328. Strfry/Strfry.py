import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = list(map(str,input().rstrip().split()))
    if ''.join(sorted(a)) == ''.join(sorted(b)):
        print('Possible')
    else:
        print('Impossible')