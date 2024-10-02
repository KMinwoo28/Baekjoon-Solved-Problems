import sys
sp = {}
lst = sys.stdin.readlines()
for s in lst:
    tg = s.strip()
    if tg in sp:
        sp[tg] += 1
    else:
        sp[tg] = 1
total = sum(sp.values())
res = sorted(sp.keys())
for i in range(len(res)):
    print('%s %.4f' %(res[i], sp[res[i]]/total*100))