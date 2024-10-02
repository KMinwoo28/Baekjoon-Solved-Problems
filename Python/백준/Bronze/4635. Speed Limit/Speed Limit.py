while True:
    n = int(input())
    if n == -1:
        break
    mileset = [[0,0]]
    total = 0
    for i in range(1,n+1):
        mileset.append(list(map(int,input().split())))
        total += mileset[i][0]*(mileset[i][1]-mileset[i-1][1])
    print(total,"miles")