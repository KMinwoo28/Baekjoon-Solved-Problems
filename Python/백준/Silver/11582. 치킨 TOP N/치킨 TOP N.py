# python으로는 느려서 merge sort를 사용할 수 없다.
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
K = int(input())
div = N // K
for i in range(0, N, div):
    sub = sorted(arr[i:i+div])
    print(*sub, end = " ")
