T = int(input())
for i in range(T):
    numList = list(map(int, input().split()))
    numList.sort()
    print(numList[-3])
    