scores = [0 for _ in range(5)]

for i in range(5):
    total = list(map(int,input().split()))
    scores[i] = sum(total)
print(scores.index(max(scores))+1,max(scores))