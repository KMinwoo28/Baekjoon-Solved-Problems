word = input().upper()
uniqueWord = list(set(word))

countList = []
for i in uniqueWord:
    count = word.count(i)
    countList.append(count)

if countList.count(max(countList)) > 1:
    print('?')
else:
    maxIndex = countList.index(max(countList))
    print(uniqueWord[maxIndex])
