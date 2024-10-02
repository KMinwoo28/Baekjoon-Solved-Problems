T = int(input())
for i in range(T):
    OX = list(input())
    score, temp = 0, 0
    for OX in OX:
        if OX == 'O':
            temp += 1
            score += temp
        else:
            temp = 0  
    print(score)
        