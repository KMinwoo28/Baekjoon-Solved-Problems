def Rev(x):
    y = str(x)[::-1]
    return int(y)
    
a, b = map(Rev,input().split())
print(Rev(a+b))