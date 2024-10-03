N = int(input())
numlist = list(map(int,input().split()))
prior = sorted(list(set(numlist)))
dic = {prior[i]:i for i in range(len(prior))}
for n in numlist:
    print(dic[n], end = " ")