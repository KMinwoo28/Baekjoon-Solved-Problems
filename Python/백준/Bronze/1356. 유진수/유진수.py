num = input()
for i in range(1,len(num)):
    fr = list(num[:i])
    re = list(num[i:])
    frmu = 1
    remu = 1
    for f in fr:
        frmu *= int(f)
    for r in re:
        remu *= int(r)
    if frmu == remu:
        print('YES')
        break
else:
    print('NO')