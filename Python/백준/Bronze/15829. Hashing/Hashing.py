alpha = 'abcdefghijklmnopqrstuvwxyz'
L = int(input())
string = input()
res = 0
for i in range(L):
    res += (alpha.index(string[i]) + 1) * (31**i)
print(res % 1234567891)