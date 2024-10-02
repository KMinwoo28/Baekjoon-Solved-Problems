N = int(input())
M = int(input())
st = input()
loc, count, res = 0,0,0
while loc < M-1:
    if st[loc:loc + 3] == 'IOI':
        count += 1
        loc += 2    # 두 칸 건너뛰기
        if count == N: # 필요한 IOI 다 찾음
            res += 1
            count -= 1
    else:
        loc += 1
        count = 0
print(res)