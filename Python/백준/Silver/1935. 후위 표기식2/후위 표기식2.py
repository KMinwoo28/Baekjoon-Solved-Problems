import sys
input = sys.stdin.readline
N = int(input())
cord = input().rstrip()
alist = {chr(65+i):int(input()) for i in range(N)}
stack = []
for c in cord:
    if c in alist:
        stack.append(alist[c])
    else:
        a = stack.pop()
        b = stack.pop()
        if c == '*':
            stack.append(b*a)
        elif c == '/':
            stack.append(b/a)
        elif c == '+':
            stack.append(b+a)
        elif c == '-':
            stack.append(b-a)
print('%.2f' %stack[0])   