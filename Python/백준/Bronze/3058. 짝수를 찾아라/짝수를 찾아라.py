T = int(input())
for _ in range(T):
    numlist = sorted(list(map(int,input().split())))
    evens = []
    for i in numlist:
        if i % 2 == 0:
            evens.append(i)
    print(sum(evens),evens[0])