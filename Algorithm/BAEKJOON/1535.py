# 재귀
def recursion(i, cur_happy, cur_hp):
    global now_happy

    if cur_hp <= 0:                         # 체력이 0이하면
        pre_happy = cur_happy - happy[i-1]  # 이전 기쁨으로 돌아가기
        if pre_happy > now_happy:           # 이전 기쁨, 현재 기쁨 중 최댓값
            now_happy = pre_happy
        return happy

    if i == N:                              # 모든 사람 만났으명
        if cur_happy > now_happy:           # 최대 기쁨 구하기
            now_happy = cur_happy
        return happy
    
    recursion(i+1, cur_happy + happy[i], cur_hp - hp[i])
    recursion(i+1, cur_happy, cur_hp)

N = int(input())
hp = list(map(int, input().split()))
happy = list(map(int, input().split()))

now_hp = 100    # 현재 체력
now_happy = 0   # 현재 기쁨

recursion(0, 0, now_hp)
print(now_happy)