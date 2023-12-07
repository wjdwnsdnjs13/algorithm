from collections import deque

def solution(cards1, cards2, goal):
    # 카드 뭉치에서 순서대로 한 장씩 사용함.
    # 다시 사용 불가.
    # 다음 카드로 못 넘어감.
    # 단어 순서 못 바꿈.
    # cards1이랑 2의 길이는 1 ~ 10
    # 단어의 길이도 1 ~ 10
    # 1이랑 2에 서로 다른 단어만 존재.
    # goal의 길이는 2 이상이고, len(1) + len(2)보다 이하임 
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    answer = "Yes"
    for g in goal:
        if(cards1 and cards1[0] == g):
            cards1.popleft()
            continue
        if(cards2 and cards2[0] == g):
            cards2.popleft()
            continue
        answer = "No"
    return answer