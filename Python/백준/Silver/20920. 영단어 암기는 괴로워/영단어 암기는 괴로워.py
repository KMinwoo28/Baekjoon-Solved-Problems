import sys
input = sys.stdin.readline
N, M = map(int,input().split())
dic = {}
for i in range(N):
    word = input().rstrip()
    if len(word)>=M:
        if word in dic.keys():
            dic[word] += 1
        else:
            dic[word] = 1
wordlist = sorted(dic.items(),key = lambda x:(-x[1],-len(x[0]),x[0]))
for s in wordlist:
    print(s[0])