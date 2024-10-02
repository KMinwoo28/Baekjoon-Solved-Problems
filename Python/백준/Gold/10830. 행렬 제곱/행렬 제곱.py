# 거듭제곱과 같은 맥락
import sys
input = sys.stdin.readline

def mul_matrix(mat1, mat2):
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for z in range(N):
                # c11 = a11*b11 + a12*b21
                res[i][j] += mat1[i][z] * mat2[z][j] % 1000
    return res

def power(a, x):
    if x == 1:  
        return a
    else:
        tmp = power(a, x // 2)  
        if x % 2 == 0:
            return mul_matrix(tmp, tmp)  
        else:
            return mul_matrix(mul_matrix(tmp, tmp), a)  

N, B = map(int,input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().split())))
res = power(matrix, B)
for row in res:
    for col in row:
        print(col % 1000, end = " ")
    print()