T= int(input())
for _ in range(T):
    P, M = map(int,input().split())
    count = 0
    seat = [0]*M
    for i in range(P):
        want = int(input())
        if seat[want-1] == 0:
            seat[want-1] = 1
        else:
            count += 1
    print(count)