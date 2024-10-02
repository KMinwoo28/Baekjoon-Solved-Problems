N = int(input())
score = [0] *301
for i in range(1, N + 1):
    score[i] = int(input())
maxscore = [0] * 301
maxscore[1] = score[1]
maxscore[2] = score[1] +score[2]
maxscore[3] = max(score[1] + score[3], score[2] + score[3])
for i in range(4, N + 1):
    maxscore[i] = max(maxscore[i - 3] + score[i - 1] +  score[i], maxscore[i - 2] + score[i])
print(maxscore[N])