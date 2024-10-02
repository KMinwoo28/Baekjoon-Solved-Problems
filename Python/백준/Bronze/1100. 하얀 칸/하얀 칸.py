import sys
input = sys.stdin.readline
chess = [list(input()) for s in range(8)]
count = 0
for i in range(0, len(chess), 2): # 홀수번 째 판
    for j in range(4):
        if chess[i][2*j] == 'F':
            count += 1
for i in range(1, len(chess), 2): # 짝수번 째 판
    for j in range(4):
        if chess[i][2*j + 1] == 'F':
            count += 1
print(count)