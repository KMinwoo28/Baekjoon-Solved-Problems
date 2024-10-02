import sys
input = sys.stdin.readline
while True:
    T = int(input())
    if T == 0:
        break
    else:
        wordlist = []
        for _ in range(T):
            wordlist.append(input().rstrip())
        switch = []
        for s in wordlist:
            switch.append(s.lower())
        print(wordlist[switch.index(min(switch))])