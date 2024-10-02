import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    stack = []
    Ev = list(input().rstrip().split())
    for E in Ev[1:]:
        if E == '0':
            stack.append(False)
        elif E == '1':
            stack.append(True)
        elif E == 'A':
            One = stack.pop()
            Two = stack.pop()
            stack.append(One and Two)
        elif E == 'R':
            One = stack.pop()
            Two = stack.pop()
            stack.append(One or Two)
        elif E == 'X':
            One = stack.pop()
            Two = stack.pop()
            stack.append(One != Two)
        elif E == 'N':
            stack.append(not stack.pop())
    print(1 if stack.pop() else 0)