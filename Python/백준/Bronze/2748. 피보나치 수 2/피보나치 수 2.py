phi = [0,1]
num = int(input())
for i in range(2,num + 1):
    phi.append(phi[i-1] + phi[i-2])
print(phi[num])