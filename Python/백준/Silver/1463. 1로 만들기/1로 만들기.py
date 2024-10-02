x= int(input())
N = [0]*(x+ 1) # 각 숫자별 필요한 연산 개수 저장 & Initialization
for i in range(2, x+1): # 2 ~ x 까지 연산 횟수 최소값 계산 (1은 연산이 0번 필요하므로 제외)
       N[i] = 1 +N[i - 1]
       if i % 2 == 0:
           N[i] = min(N[i], N[i//2] + 1) # 두 개 중 연산 횟수가 적은 쪽을 택한다.
       if i % 3 == 0: 
               N[i] = min(N[i], N[i//3] + 1)      
print(N[x]) 
