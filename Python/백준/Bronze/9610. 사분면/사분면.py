T = int(input())
dot_location = [0,0,0,0,0]
for _ in range(T):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        dot_location[-1] += 1
    elif x>0:
        if y>0:
            dot_location[0] += 1
        else:
            dot_location[3] += 1
    else:
        if y<0:
            dot_location[2] += 1
        else:
            dot_location[1] += 1
print('Q1:',dot_location[0])
print('Q2:',dot_location[1])
print('Q3:',dot_location[2])
print('Q4:',dot_location[3])
print('AXIS:',dot_location[4])