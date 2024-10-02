mel = list(map(int,input().split()))
height = 0
for i in range(7):
    if mel[i] < mel[i+1]:
        height += 1
    elif mel[i] >mel[i+1]:
        height -= 1
if height == 7:
    print('ascending')
elif height == -7:
    print('descending')
else:
    print('mixed')