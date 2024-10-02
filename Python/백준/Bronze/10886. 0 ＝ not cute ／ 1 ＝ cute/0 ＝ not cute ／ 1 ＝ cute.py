N = int(input())
vote_list = []
for _ in range(N):
    vote_list.append(int(input()))
if vote_list.count(1)>vote_list.count(0):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')