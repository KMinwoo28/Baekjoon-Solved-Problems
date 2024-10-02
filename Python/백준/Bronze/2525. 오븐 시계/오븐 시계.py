a, b = map(int,input().split())
time = a * 60 + b
load = int(input())
print(((time + load)//60)%24,(time + load)%60)