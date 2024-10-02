chess = list(map(int,input().split()))
need = [1,1,2,2,2,8]
for i in range(6):
    print(need[i] - chess[i], end = " ")