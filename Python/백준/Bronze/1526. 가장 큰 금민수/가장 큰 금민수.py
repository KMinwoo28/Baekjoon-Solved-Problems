import re
T = int(input())
for i in range(T,3,-1):
    if re.fullmatch('(4|7)+',str(i)):
        print(i)
        break