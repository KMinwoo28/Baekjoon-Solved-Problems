import sys
input = sys.stdin.readline
N = int(input())
FN = [input()[0] for s in range(N)]
sunglist = list(set(FN))
available = []
for s in sunglist:
    if FN.count(s) >= 5:
        available.append(s)
available.sort()
if available == []:
    print("PREDAJA")
else:
    print(''.join(available))