# No comment version
import sys
input = sys.stdin.readline
K,D,A = map(int,input().split('/'))
if K+A <D or D == 0:
    print('hasu')
else:
    print('gosu')