button = [0,0,0]
time = int(input())
while(True):
    if time >= 300:
        button[0] += 1
        time -= 300
    elif time >= 60:
        button[1] += 1
        time -= 60
    elif time >= 10:
        button[2] += 1
        time -= 10
    elif time > 0:
        print(-1)
        break
    else:
        print(button[0],button[1],button[2])
        break