T = int(input())
for _ in range(T):
    M, N = map(int,input().split())
    priority = list(map(int,input().split()))
    output = [i for i in range(M)]
    count = 0
    while True:
        if priority[0] == max(priority):
            count += 1
            if output[0] == N:
                print(count)
                break
            else:
                del priority[0]
                del output[0]
        else:
            priority.append(priority[0])
            del priority[0]
            output.append(output[0])
            del output[0]