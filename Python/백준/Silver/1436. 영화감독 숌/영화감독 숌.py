N = int(input())
title = 600
series = 0
latest = 0
while series < N:
    if str(title).count('666')>= 1:
        latest = title
        series += 1
    title += 1
print(latest)