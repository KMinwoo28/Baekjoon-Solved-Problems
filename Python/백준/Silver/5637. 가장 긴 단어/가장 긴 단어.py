import sys
import re
input = sys.stdin.readline
cond = re.compile(r'[a-zA-z-]+')
long = 0
word = ''
e = False
while True:
    words = cond.findall(input())
    for w in words:
        if w == 'E-N-D':
            e = True
            break
        if len(w)>long:
            word = w
            long = len(w)
    if e:
        print(word.lower())
        break