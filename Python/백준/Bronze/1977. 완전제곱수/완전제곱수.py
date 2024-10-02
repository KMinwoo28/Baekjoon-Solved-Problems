a= int(input())
b = int(input())
perfect = []
for i in range(a, b+1):
    root = int(i ** 0.5)
    if i == root ** 2:
        perfect.append(i)
        
if perfect == []:
    print(-1)
else:
    print(sum(perfect))
    print(min(perfect))