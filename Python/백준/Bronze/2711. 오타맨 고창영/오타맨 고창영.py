T = int(input())
for _ in range(T):
    loc, word = input().split()
    print(word[:int(loc)-1]+word[int(loc):])