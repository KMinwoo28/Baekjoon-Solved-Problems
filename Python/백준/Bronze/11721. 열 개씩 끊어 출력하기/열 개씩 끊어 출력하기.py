# 11721 열 개씩 끊어 출력하기 201902089 곽민우
word = input()
line = len(word) // 10 + 1
for i in range(line):
    print(word[10*i:10*i+10])