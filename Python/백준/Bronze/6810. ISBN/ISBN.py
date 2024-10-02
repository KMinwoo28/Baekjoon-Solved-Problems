import sys
input = sys.stdin.readline
init = 91
for i in range(3):
    if i % 2 == 0:
        init += int(input()) * 1
    else:
        init += int(input()) * 3
print(f'The 1-3-sum is {init}')