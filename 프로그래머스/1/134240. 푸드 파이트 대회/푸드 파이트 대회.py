def solution(food):
    # 1:1 대결
    # 대결마다 매번 음식 종류와 양이 바뀜
    # A는 왼쪽에서, B는 오른쪽에서 중앙으로 옴
    # 준비된 음식 중 못 먹게 되는 게 있음.
    # 물이 항상 가운데 옴.
    # 음식을 배치하셈.
    player = "".join([str(i) * (food[i]//2) for i in range(1, len(food))])
    answer = player + "0" + player[::-1]
    return answer