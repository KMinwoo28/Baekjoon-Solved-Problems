H,M = map(int,input().split())
time = (H*60 + M)+ 1395
print(f"{(time//60)%24} {time%60}")