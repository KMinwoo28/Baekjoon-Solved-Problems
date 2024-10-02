import sys
input = sys.stdin.readline

color = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
idx = ['0','1','2','3','4','5','6','7','8','9']
multiple = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]
a = input().rstrip()
b = input().rstrip()
c = input().rstrip()
print(int(idx[color.index(a)]+idx[color.index(b)])*multiple[color.index(c)])