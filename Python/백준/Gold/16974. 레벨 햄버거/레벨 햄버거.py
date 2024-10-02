def eaten_patty(L, ate):
    if ate == 1: # 맨 아래 빵만 먹었다...
        return 0
    if ate < layer[L - 1] + 1: # 먹은 게 L-1레벨 버거, 바닥 빵 미만이면
        return eaten_patty(L - 1, ate - 1) # 바닥 빵을 빼고 L-1 레벨 버거 안에서.
    if ate == layer[L - 1] + 1: # 먹은 게 L-1레벨 버거, 바닥 빵이면
        return patty[L - 1] # L-1 레벨 버거의 패티 수.
    if ate == layer[L - 1] + 2: # 먹은 게 L-1레벨 버거, 바닥 빵, 중간 패티이면
        return patty[L - 1] + 1 # L-1 레벨 버거의 패티 수 + 1.
    if ate <  2*layer[L - 1] + 2: # 바닥 빵, L-1 레벨 버거, 중간 패티, L-1 레벨 버거 일부 먹음
        return patty[L - 1] + 1 + eaten_patty(L - 1, ate - layer[L-1] - 2)
        # 바닥 L-1 레벨 버거, 중간 패티, 이 둘을 제외한 위의 L-1 레벨 버거의 일부 계산
        # (ate에서 바닥 layer 값, layer[L - 1]+ 2를 빼고 넣어야 한다.)
    # 버거를 전부 먹거나, 가장 위 번을 안먹은 경우
    return patty[L]

L, ate = map(int,input().split())
layer = [0] * (L + 1) # Number of Layer, 레벨 별 개수 위치
patty = [0] * (L + 1) # Number of Patty, 레벨 별 개수 위치
layer[0] = patty[0] = 1 # 0레벨 버거는 패티 한 장
# 레벨 L-버거 : 번 + 레벨 L-1 버거 + 패티 + 레벨 L-1 버거 + 번
for i in range(1, L + 1): # 위의 식을 대입
    layer[i] = 3 + 2*layer[i - 1]
    patty[i] = 1 + 2*patty[i - 1]
print(eaten_patty(L, ate))