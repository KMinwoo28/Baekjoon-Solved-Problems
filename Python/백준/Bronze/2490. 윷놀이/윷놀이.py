for _ in range(3):
    yoot = list(map(int,input().split()))
    ycount = yoot.count(0)
    if ycount == 0:
        print('E')
    elif ycount == 1:
        print('A')
    elif ycount == 2:
        print('B')
    elif ycount == 3:
        print('C')
    else:           #ycount == 4
        print('D')
