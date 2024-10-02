sc = ['Soongsil', 'Korea', 'Hanyang']
pa = list(map(int,input().split()))
if sum(pa)>= 100:
    print('OK')
else:
    print(sc[pa.index(min(pa))])