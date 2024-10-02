res = []
for i in range(1,6):
    name = input()
    if 'FBI' in name:
        res.append(i)
if len(res) != 0:
    print(*res)
else:
    print('HE GOT AWAY!')