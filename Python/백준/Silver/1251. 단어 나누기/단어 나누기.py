import sys
input = sys.stdin.readline
s = input().rstrip()
switched = []
for i in range(len(s)-2):
    for j in range(i+1,len(s)-1):
        a, b, c = s[:i+1],s[i+1:j+1],s[j+1:]
        switched.append(a[::-1]+b[::-1]+c[::-1])
            
switched.sort()
print(switched[0])