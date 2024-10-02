T = int(input())
for _ in range(T):
    sub = int(input())
    hak = 0
    score = 0
    for i in range(sub):
        a, b = map(float,input().split())
        hak += int(a)
        score += a*b
    print(f"{hak} {round(score/hak,1)}")