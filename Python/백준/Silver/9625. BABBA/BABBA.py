K = int(input())
dpa = [0] * 46 # 버튼을 눌렀을 때 A의 개수
dpb = [0] * 46 # 버튼을 눌렀을 때 B의 개수
# Initialization
dpa[0] = 1 
dpb[0] = 0
for i in range(1, K+1):
    dpa[i] = dpb[i - 1]
    dpb[i] = dpa[i -1] + dpb[i-1]
print(dpa[K], dpb[K])