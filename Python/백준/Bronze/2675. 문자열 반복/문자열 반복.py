T = int(input())
for i in range(T):
    rep, word = input().split()
    rep = int(rep)
    for j in word:
        print(rep*j, end = "")
    print()    