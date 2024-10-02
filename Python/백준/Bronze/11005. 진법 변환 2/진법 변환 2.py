digit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num, zin = map(int,input().split())
res = ''
while(num):
    res += digit[num % zin]
    num //= zin
print(res[::-1])