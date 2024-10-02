def prime_num(num):
    if num != 1:
        for i in range(2, num):
            if num % i == 0:
                return False
    else:
        return False
    return True

a = int(input())
b = int(input())
prime = []
for i in range(a,b+1):
    if prime_num(i):
        prime.append(i)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])