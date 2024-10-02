N = int(input())
yaklist = list(map(int,input().split()))
yaklist.sort()
print(yaklist[0]*yaklist[-1])