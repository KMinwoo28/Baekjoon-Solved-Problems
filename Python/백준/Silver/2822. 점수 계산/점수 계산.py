scorelist = []
for _ in range(8):
    scorelist.append(int(input()))
highscore = sorted(scorelist,reverse = True)
print(sum(highscore[:5]))
indexes = []
for i in range(5):
    indexes.append(scorelist.index(highscore[i]))
indexes.sort()
for j in range(5):
    print(indexes[j] + 1, end = " ")