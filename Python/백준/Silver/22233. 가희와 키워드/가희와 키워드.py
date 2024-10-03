import sys
input = sys.stdin.readline
N, M = map(int,input().split())
note = {input().rstrip(): 0 for _ in range(N)}
for _ in range(M):
    art = list(map(str,input().rstrip().split(',')))
    for a in art:
        if a in note:
            note.pop(a)
    print(len(note))