ki = []
for _ in range(9):
    ki.append(int(input()))
ki.sort()
comp = False
for i in range(8):
    for j in range(i+1,9):
        if sum(ki)-ki[i]-ki[j] == 100:
            del ki[i]
            del ki[j-1]
            comp = True
            break
    if comp:
        break
for k in range(7):
    print(ki[k])