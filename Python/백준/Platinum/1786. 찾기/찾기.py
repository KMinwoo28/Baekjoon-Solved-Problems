import sys
input = sys.stdin.readline
def make_kmp_table(pattern, border):
    m = len(pattern)
    border[0] = -1
    i = 2
    cnd = 0
    while i < m:
        if pattern[i-1] == pattern[cnd]:
            cnd += 1
            border[i] = cnd
            i += 1
        elif cnd > 0:
            cnd = border[cnd] 
        else:
            border[i] = 0
            i += 1
    return border
def kmp_search(pattern, border, text, res):
    m = 0
    i = 0
    t_len = len(text)
    p_len = len(pattern)
    
    while m+i<t_len:
        if pattern[i] == text[m+i]:
            if i == p_len - 1:
                res.append(m+1)
                m = m + i - border[i]
                i = border[i]
                continue
            i += 1
        else:
            if border[i] > -1:
                m = m + i - border[i]
                i = border[i]
            else:
                i = 0
                m += 1
    return res

T = input().rstrip()
P = input().rstrip()
border = [0]*len(P)
res = []
border = make_kmp_table(P, border)
res = kmp_search(P, border, T, res)
print(len(res))
print(*res)