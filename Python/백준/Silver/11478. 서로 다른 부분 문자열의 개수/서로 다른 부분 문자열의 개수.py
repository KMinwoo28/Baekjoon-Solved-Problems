word = input()
makeset = set()
for i in range(len(word)):
    for j in range(i,len(word)):
        makeset.add(word[i:j+1])
print(len(makeset))