def prime_num(num):
    if num != 1:
        for i in range(2, num):
            if num % i == 0:
                return False
    else:
        return False
    return True

a = int(input())
numlist = list(map(int,input().split()))
count = 0
for i in numlist:
    if prime_num(i):
        count += 1
print(count)