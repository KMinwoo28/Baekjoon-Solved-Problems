F = input()
dic = {}
for f in F:
    if f in dic:
        dic[f] += 1
    else:
        dic[f] = 1
keys = sorted(dic.keys())
odd_alpha = ''
valid =True
for key in keys:
    if dic.get(key) % 2 == 1:
        if odd_alpha == '':
            odd_alpha = key
        else: # Invalid
            valid = False
            break
else:
    fal = []
    for key in keys:
        fal.append(key * (dic[key] // 2))
    print(''.join(fal) + odd_alpha + ''.join(reversed(fal)))
if not valid:
    print('I\'m Sorry Hansoo')