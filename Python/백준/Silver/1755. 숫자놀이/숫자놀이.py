import sys
input = sys.stdin.readline
M, N = input().split()
alpha = ['zero','one','two','three','four','five','six','seven','eight','nine']
dic = {}
for num in range(int(M), int(N)+1):
    if len(str(num)) == 2:
        dic[num] = alpha[int(str(num)[0])] + alpha[int(str(num)[1])]
    else:
        dic[num] = alpha[num]
res = sorted(dic.items(), key = lambda x:x[1])
count = 0
for i in range(len(res)):
    print(res[i][0], end = " ")
    count += 1
    if count % 10 == 0:
        print()