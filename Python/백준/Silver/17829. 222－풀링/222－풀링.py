import sys
input = sys.stdin.readline
def two_pooling(mat, N):
    if N == 1:
        return mat[0][0]
    sub_mat = [[] for _ in range(N//2)]
    for i in range(0,N,2): # 2*2로 슬라이싱
        for j in range(0,N,2):
            insert = sorted([mat[i][j],mat[i][j+1],mat[i+1][j],mat[i+1][j+1]])
            sub_mat[i//2].append(insert[2])# 두번째로 큰 값만 추가
    return two_pooling(sub_mat, N//2)
    
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
print(two_pooling(matrix, N))