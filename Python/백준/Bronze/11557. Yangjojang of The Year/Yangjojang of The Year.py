T = int(input())
for i in range(T):
    N = int(input())
    Dict = dict()
    for j in range(N):
        univ, drink = input().split()
        Dict[int(drink)] = univ
    print(Dict[max(Dict.keys())])