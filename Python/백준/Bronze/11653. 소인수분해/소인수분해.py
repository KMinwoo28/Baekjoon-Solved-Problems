num = int(input())
for i in range(2, num + 1):
    while(True):
        if num % i == 0:
            print(i)
            num = num / i
        else:
            break;