n = int(input())
count = 0
i = 0
numlist = []
while(count < n):
    num = int(input()) 
    if  num != 0:
        numlist.append(num)
        i += 1
    else:
        if i != 0:
            del numlist[i-1]
            i -= 1
    count += 1
print(sum(numlist))