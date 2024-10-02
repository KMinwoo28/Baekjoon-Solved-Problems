bowl = input()
bowlLen = 10
for i in range(1, len(bowl)):
    if bowl[i-1] == bowl[i]:
        bowlLen += 5
    else:
        bowlLen += 10
print(bowlLen)
        