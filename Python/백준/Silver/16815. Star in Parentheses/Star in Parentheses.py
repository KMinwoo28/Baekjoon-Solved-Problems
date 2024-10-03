string = input()
count = 0
string = string.replace("()","")
loc = string.index('*')
i = 1
try:
    while True:
        if string[loc-i] == "(" and string[loc + i] == ")":
            count += 1
        i += 1
except:
    print(count)