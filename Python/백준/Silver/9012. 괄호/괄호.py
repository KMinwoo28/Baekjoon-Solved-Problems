import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    PS = input().rstrip()
    stack = []
    for ps in PS:
        if ps == '(':
            stack.append(ps)
        elif ps == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')