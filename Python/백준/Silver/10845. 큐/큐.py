import sys
input = sys.stdin.readline
N = int(input())
Q = []
count = 0
for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        Q.append(int(order[1]))
    elif order[0] == 'pop':
        if len(Q) - count == 0:
            print(-1)
        else:
            print(Q[count])
            count += 1
    elif order[0] == 'size':
        print(len(Q)- count)
    elif order[0] == 'empty':
        print(1) if len(Q) - count == 0 else print(0)
    elif order[0] == 'front':
        print(Q[count]) if len(Q)- count != 0 else print(-1)
    elif order[0] == 'back':
        print(Q[-1]) if len(Q)- count != 0 else print(-1) 