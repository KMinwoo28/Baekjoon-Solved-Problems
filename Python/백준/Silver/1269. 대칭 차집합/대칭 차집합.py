import sys
input = sys.stdin.readline
s1, s2 = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
A_B = A-B
B_A = B-A
print(len(A_B)+len(B_A))