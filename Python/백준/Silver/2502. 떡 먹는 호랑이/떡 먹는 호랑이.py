D, K = map(int,input().split())
fin = [0, 1, 1]
for _ in range(D-3):
    fin.append(fin[-1] + fin[-2])
a = fin[D-2]; b = fin[D-1]
breaker = False
for A in range(1, K+1):
    for B in range(A,K+1):
        if a*A + b*B == K:
            print(A)
            print(B)
            breaker = True
            break
    if breaker:
        break