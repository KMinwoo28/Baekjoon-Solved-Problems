stat = list(map(int,input().split()))
N = stat.pop()
need = 4*N-sum(stat)
print(need if need >= 0 else 0)