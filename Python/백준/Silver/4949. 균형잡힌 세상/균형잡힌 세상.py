import sys
input = sys.stdin.readline
while True:
    sentence = input().rstrip()
    if len(sentence) == 1 and sentence == '.':
        break
    sentence = list(sentence)
    stack = []
    balanced = True
    for s in sentence:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if len(stack) == 0:
                balanced = False
                break
            else:
                if stack[-1] != "(":
                    balanced = False
                    break
                else:
                    del stack[-1]
        elif s == "]":
            if len(stack) == 0:
                balanced = False
                break
            else:
                if stack[-1] != "[":
                    balanced = False
                    break
                else:
                    del stack[-1]
    if balanced and len(stack) == 0:
        print('yes')
    else:
        print('no')