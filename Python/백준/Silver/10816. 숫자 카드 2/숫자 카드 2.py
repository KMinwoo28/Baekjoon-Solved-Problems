import sys
input = sys.stdin.readline
N = int(input())
Have = list(map(int,input().split()))
M = int(input())
Q = list(map(int,input().split()))
card = {}
for h in Have:
    if h in card:
        card[h] += 1
    else:
        card[h] = 1
for q in Q:
    if q in card:
        print(card[q], end = ' ')
    else:
        print(0, end = ' ')