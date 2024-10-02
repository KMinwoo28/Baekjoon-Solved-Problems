# 10987 모음의 개수 201902089 곽민우
word = input()
vowelcount = 0
for i in range(len(word)):
    if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
        vowelcount += 1
print(vowelcount)