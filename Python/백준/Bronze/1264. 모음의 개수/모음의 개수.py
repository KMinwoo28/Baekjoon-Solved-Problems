import sys
input = sys.stdin.readline
def isvowel(string):
    vowel = ['a','e','i','o','u']
    if string in vowel:
        return True
    else:
        return False
while True:
    sent = input().rstrip().lower()
    if sent == '#':
        break
    count = 0
    for s in sent:
        if isvowel(s):
            count += 1
    print(count)