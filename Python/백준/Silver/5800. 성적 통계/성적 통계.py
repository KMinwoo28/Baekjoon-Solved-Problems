K = int(input())
for I in range(K):
    arr = list(map(int,input().split()))
    N = arr[0]
    score = sorted(arr[1:],reverse = True)
    gap = 0
    for i in range(N-1):
        if score[i]-score[i+1]>gap:
            gap = score[i]-score[i+1]
    print("Class",I+1)        
    print(f"Max {score[0]}, Min {score[-1]}, Largest gap {gap}")