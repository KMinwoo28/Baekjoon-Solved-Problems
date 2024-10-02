vowel = ['a','e','i','o','u']
T = int(input())
for _ in range(T):
    c, v = 0, 0
    st = input().lower().replace(" ","")
    for s in st:
        if s in vowel:
            v += 1
        else:
            c += 1
    print(c, v)