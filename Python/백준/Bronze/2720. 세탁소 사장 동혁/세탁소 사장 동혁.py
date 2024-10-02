Coin = [25, 10, 5, 1]
T = int(input())
for _ in range(T):
    C = int(input())
    
    for i in range(4):
        print(C//Coin[i], end = " ")
        C %= Coin[i]
    print()