dice = list(map(int,input().split()))
dice.sort()
if dice[0] == dice[1] and dice[1] == dice[2]:
    print(10000+ dice[0] * 1000)
elif (dice[0] == dice[1] and dice[1] !=dice[2]) or(dice[0] == dice[2] and dice[0] !=dice[1]):
    print(1000 + dice[0] * 100)
elif dice[0] != dice[1] and dice[1] ==dice[2]:
    print(1000 + dice[1] * 100)
else:
    print(dice[2] * 100)