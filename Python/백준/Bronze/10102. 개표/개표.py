pers = int(input())
grade = input()
aScore, bScore = 0 , 0
for i in range(pers):
    if grade[i] == 'A':
        aScore += 1
    elif grade[i] == 'B':
        bScore += 1
if aScore > bScore:
    print('A')
elif aScore < bScore:
    print('B')
else:
    print('Tie')
 