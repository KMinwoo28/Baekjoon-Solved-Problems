pay = 1000 - int(input())
m = [500, 100, 50, 10, 5, 1]
t = 0
for i in range(6):
    t += pay // m[i]
    pay %= m[i]
print(t)