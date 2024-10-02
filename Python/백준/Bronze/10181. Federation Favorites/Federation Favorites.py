while(True):
    numlist = []
    target = int(input())
    if target == -1:
        break
    sum = 0
    for i in range(1,target):
        if target % i == 0:
            numlist.append(i)
            sum += i
    if sum == target:
        print(target, end =' = ')
        for j in range(len(numlist) - 1):
            print(numlist[j],end = ' + ')
        print(numlist[-1])
    else:
        print(target,'is NOT perfect.')