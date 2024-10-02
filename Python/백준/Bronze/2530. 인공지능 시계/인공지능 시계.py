a,b,c = map(int,input().split())
time = a*3600 + b*60 + c
load = time + int(input())
print((load // 3600)%24,(load//60)%60, load % 60)