import sys
input = sys.stdin.readline
T = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
A = input().rstrip()
B = input().rstrip()
arr = []
for i in range(len(A)):
	arr.append(T[ord(A[i]) - 65])
	arr.append(T[ord(B[i]) - 65])
res = []
while len(arr) != 2:
    for i in range(len(arr)-1):
        res.append((arr[i] + arr[i+1]) % 10)
    arr = res
    res = []
print(f'{arr[0]}{arr[1]}')