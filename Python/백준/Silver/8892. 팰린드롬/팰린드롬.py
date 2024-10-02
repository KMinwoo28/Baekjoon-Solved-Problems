T = int(input())
for _ in range(T):
    n = int(input())
    lst = [input() for _ in range(n)]
    maked = False
    for i in range(n-1):
        for j in range(i+1,n):
            make1 = lst[i]+lst[j]
            make2 = lst[j]+lst[i]
            cp1 = make1[::-1]
            cp2 = make2[::-1]
            if make1 == cp1:
                maked = True
                print(make1)
                break
            elif make2 == cp2:    
                maked = True
                print(make2)
                break
        if maked:
            break
    if maked == False:
        print(0)