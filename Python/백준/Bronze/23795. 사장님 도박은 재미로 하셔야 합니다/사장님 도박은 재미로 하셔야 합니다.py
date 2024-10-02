import sys
input = sys.stdin.readline
lost = 0
bat = int(input())
while bat != -1:
    lost += bat
    bat = int(input())
print(lost) 