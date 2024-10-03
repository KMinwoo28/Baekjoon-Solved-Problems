import sys
input = sys.stdin.readline
target = list(input().rstrip())
stack = []
wordloc = 0

for i in range(len(target)):
    if '<' in stack:
        if target[i] == '>':
            stack.pop()
            wordloc = i+1
    else:
        if target[i] == '<':
            stack.append('<')
            target[wordloc:i] = target[wordloc:i][::-1] 
            wordloc = i+1
            continue
        elif target[i] == ' ':
            target[wordloc:i] = target[wordloc:i][::-1] 
            wordloc = i+1
if stack == []: # switch last word
    target[wordloc:] = target[wordloc:][::-1]
print(''.join(target))   