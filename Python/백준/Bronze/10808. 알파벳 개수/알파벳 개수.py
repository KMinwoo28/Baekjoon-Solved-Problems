alpha = 'abcdefghijklmnopqrstuvwxyz'
loc = [0]*26
word = input()
for s in word:
    loc[alpha.index(s)] += 1
print(*loc)