import sys
input = sys.stdin.readline

def cycle(num):
    if num < 10:
        temp = ['0',str(num)]
    else:
        temp = list(str(num))
    hap = int(temp[0]) + int(temp[1])
    new = 10*int(temp[1])+ (hap % 10)
    return new
        

first = int(input())
time = 0
change = first
change = cycle(change)
if change == first:
    print(1)
else:
    time += 1
    while(change != first):
        change = cycle(change)
        time += 1
    print(time)