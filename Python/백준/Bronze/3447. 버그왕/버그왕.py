import sys
sentence = sys.stdin.readlines()
for word in sentence:
    while True:
        word = word.replace('BUG','')
        
        if 'BUG' in word:
            continue
        else:
            print(word, end = "")
            break