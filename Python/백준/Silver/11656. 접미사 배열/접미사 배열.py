import sys
input = sys.stdin.readline
string = input().rstrip()
rearlist = []
for s in range(len(string)):
    rearlist.append(string[s:])
rearlist.sort()
for s in rearlist:
    print(s)