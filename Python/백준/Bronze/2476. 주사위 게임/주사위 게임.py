N = int(input())
award_list = []
for _ in range(N):
    dice = list(map(int,input().split()))
    dice.sort()
    if dice[0] == dice[1] and dice[1] == dice[2]:
        award_list.append(10000+ dice[0] * 1000)
    elif (dice[0] == dice[1] and dice[1] !=dice[2]) or(dice[0] == dice[2] and dice[0] !=dice[1]):
        award_list.append(1000 + dice[0] * 100)
    elif dice[0] != dice[1] and dice[1] ==dice[2]:
        award_list.append(1000 + dice[1] * 100)
    else:
        award_list.append(dice[2] * 100)
print(max(award_list))