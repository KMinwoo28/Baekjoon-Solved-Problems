T = int(input())
for _ in range(T):
    cal = list(map(str, input().split()))
    ans = 0
    for i in range(len(cal)):
        if i == 0:
            ans += float(cal[i])
        else:
            if cal[i] == '#':
                ans -= 7
            elif cal[i] == "%":
                ans += 5
            elif cal[i] == '@':
                ans *= 3            
    print('%.2f' %ans)