import sys
input = sys.stdin.readline

numlist = []
for i in range(9):
    numlist.append(list(map(int,input().split())))
maxrow = 0
maxcol = 0
maxval = -1
for i in range(9):
    for j in range(9):
        if numlist[i][j] > maxval:
            maxval = numlist[i][j]
            maxrow = i
            maxcol = j
print(maxval)
print(maxrow+1, maxcol+1)