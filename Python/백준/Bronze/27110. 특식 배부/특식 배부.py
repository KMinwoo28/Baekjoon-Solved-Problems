N = int(input())
need = list(map(int,input().split()))
t = 0
for i in range(3):
    t += (need[i] if need[i]< N else N)
print(t)