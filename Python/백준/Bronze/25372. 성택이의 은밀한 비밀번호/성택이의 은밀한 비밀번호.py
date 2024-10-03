N = int(input())
for _ in range(N):
    s = input()
    print('yes' if len(s)>= 6 and len(s)<= 9 else 'no')