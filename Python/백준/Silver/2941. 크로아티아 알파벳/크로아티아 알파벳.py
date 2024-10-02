Kc = ['c=','c-','dz=','d-','lj','nj','s=','z=']
string = input()
count = 0
for i in range(8):
    while Kc[i] in string:
        string = string.replace(Kc[i]," ",1)
        count += 1
string = string.replace(" ","")
print(len(string)+count)