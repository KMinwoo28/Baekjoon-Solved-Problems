T = int(input())
for _ in range(T):
    score_list = [0,0]
    for i in range(9):
        y, k = map(int, input().split())
        score_list[0] += y
        score_list[1] += k
    print('Yonsei') if score_list[0]>score_list[1] else(print('Korea') if score_list[0]>score_list[1] else print('Draw'))