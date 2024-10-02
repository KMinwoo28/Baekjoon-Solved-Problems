num = [i for i in range(1,31)]
for i in range(28):
    num.remove(int(input()))
num.sort()
print(num[0])
print(num[1])