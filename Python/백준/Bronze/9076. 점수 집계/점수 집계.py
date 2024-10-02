T= int(input())
for _ in range(T):
    scores = list(map(int,input().split()))
    scores.sort()
    if scores[3]-scores[1] >= 4:
        print('KIN')
    else:
        print(sum(scores[1:4]))