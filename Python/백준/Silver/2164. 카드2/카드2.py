# deque을 사용한 풀이
from collections import deque
n = int(input())
cards = deque([i for i in range(1,n+1)])
while(len(cards)>1):
    cards.popleft()
    temp = cards.popleft()
    cards.append(temp)
    
print(cards[0])