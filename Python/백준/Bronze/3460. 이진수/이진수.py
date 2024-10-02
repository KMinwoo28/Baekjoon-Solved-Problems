# 3460 이진수 230911 201902089 곽민우
T = int(input())
for _ in range(T):
    bin_num = format(int(input()), 'b')
    for i in range(1, len(bin_num)+ 1):
        if bin_num[-i] == '1':
            print(i-1, end = ' ')