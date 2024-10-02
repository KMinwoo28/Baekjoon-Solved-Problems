n = int(input())
phi = [0,1]
for i in range(2,n+1):
    phi.append(phi[i-2]+phi[i-1])
print(phi[n])