T = int(input())
for _ in range(T):
    dis = []
    word1, word2 = input().split()
    for i in range(len(word1)):
        if ord(word2[i])-ord(word1[i]) >= 0:
            dis.append(ord(word2[i])-ord(word1[i]))
        else:
            dis.append(26+ord(word2[i])-ord(word1[i]))
    print('Distances:',*dis)