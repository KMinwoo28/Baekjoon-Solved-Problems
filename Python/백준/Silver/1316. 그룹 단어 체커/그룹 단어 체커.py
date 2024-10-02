T = int(input())
count = 0
for _ in range(T):
    strlist = []
    iscontinue = True
    string = list(input())
    strlist.append(string[0])
    for i in range(1,len(string)):
        if string[i-1] == string[i]:
            continue
        elif string[i] not in strlist:
            strlist.append(string[i])
        else:
            iscontinue = False
            break
    if iscontinue:
        count += 1
print(count)