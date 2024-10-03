import re
cond = re.compile('.*[U]{1}.*[C]{1}.*[P]{1}.*[C]{1}.*')
target = input().replace(" ",'')
if cond.fullmatch(target):
    print('I love UCPC')
else:
    print('I hate UCPC')