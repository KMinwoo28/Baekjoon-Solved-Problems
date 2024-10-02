import sys
input = sys.stdin.readline
N = int(input())
serialList = []
for _ in range(N):
    serial = input().rstrip()
    numbers = 0
    for num in list(serial):
        if num.isdigit():
            numbers += int(num)
    serialList.append([serial,numbers])
serialList.sort(key = lambda x:(len(x[0]),x[1],x[0]))
for s in serialList:
    print(s[0])