hap = 1
for i in range(3):
    hap *= int(input())
numlist = [0,0,0,0,0,0,0,0,0,0]
hap = str(hap)
for i in range(10):
    numlist[i] = hap.count(str(i))
    print(numlist[i])