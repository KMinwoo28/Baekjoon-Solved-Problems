n, k = map(int,input().split())
res = 0
while bin(n).count('1') > k:
    loc = bin(n)[::-1].index('1')
    res += 2 ** loc # 필요한 물병 갯수를 결과에 추가 
    n += 2 ** loc # 필요한 만큼 물병을 사서 채운다.
print(res)