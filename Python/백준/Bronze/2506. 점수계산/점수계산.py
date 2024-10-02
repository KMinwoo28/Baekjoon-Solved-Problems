N = int(input())
ans = list(map(str, input().split()))
score = 0
chain = 0
for i in range(len(ans)):
    if ans[i] == '1':
        chain += 1
        score += chain
    else:
        chain = 0
print(score)