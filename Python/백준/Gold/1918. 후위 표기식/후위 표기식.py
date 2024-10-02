operator = ['+','-','*','/']
def priority(op):
    if op in operator:
        return operator.index(op)//2 + 2
    else:
        return 0 # stack's bottom
stack = ['$']
InString = input()
for f in InString:
    if f.isalpha():
        print(f, end = '')
    if f in operator:
        while priority(stack[-1]) >= priority(f):
            print(stack.pop(-1), end = '')
        stack.append(f)
    if f == "(":
        stack.append(f)
    if f == ")":
        while stack[-1] != '(':
            print(stack.pop(), end = '')
        stack.pop()
while len(stack) > 1:
    print(stack.pop(), end = '')