alpha = "abcdefghijklmnopqrstuvwxyz"
loc = [-1]*26
S = input()
for s in S:
    if loc[alpha.index(s)] == -1:
        loc[alpha.index(s)] = S.index(s)
print(*loc)