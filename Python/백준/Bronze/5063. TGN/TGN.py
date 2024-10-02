N = int(input())
for _ in range(N):
    r, e, c = map(int,input().split())
    print('advertise') if r<e-c else (print('do not advertise') if r>e-c else print('does not matter'))