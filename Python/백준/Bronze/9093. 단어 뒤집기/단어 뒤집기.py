T = int(input())
for _ in range(T):
    sent = list(map(str,input().rstrip().split()))
    for i in range(len(sent)):
        sent[i] = sent[i][::-1]
    print(' '.join(sent))