# 1 2 2 3 3 3 4 4 4 4  5  5   5  5  5  6
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
a, b = map(int,input().split())
arr = [0]
for i in range(46):     # a,b 범위는 1000까지이므로
    for j in range(i):
        arr.append(i)
print(sum(arr[a:b+1]))