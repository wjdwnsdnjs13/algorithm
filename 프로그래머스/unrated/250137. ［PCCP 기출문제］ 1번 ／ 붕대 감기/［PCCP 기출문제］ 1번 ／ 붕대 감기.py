def solution(bandage, health, attacks):
    # 붕대 감기는 t초동안 x/s 체력을 회복함.
    # t초 연속으로 붕대 감으면 y만큼 추가 회복
    # 최대 체력 초과는 안됨.
    # 공격당하면 기술 취소됨. (공격 당하는 순간은 회복x)
    # 붕대 감기 취소되면 바로 다시 사용함. 성공 시간 0초로 초기화
    # 체력 0 이하되면 사망
    # bandage = [시전 시간, 초당 회복량, 추가 회복량]
    # attacks[i] = [공격 시간, 피해량] # 공격 시간을 기준으로 오름차순 정렬됨.
    
    # attacks를 for문 돌리기.
    hp = health
    for i in range(len(attacks)):
        hp -= attacks[i][1]
        if(hp <= 0):
            return -1
        if(i < len(attacks) - 1):
            # 붕대를 감을 시간은 이번 공격 시간부터 과 다음 공격 직전 시간까지
            time = attacks[i + 1][0] - attacks[i][0] - 1
            # 붕대 감은 초 만큼 회복, 1회 완료마다 추가 회복
            healing = (time * bandage[1]) + (time//bandage[0] * bandage[2])
            hp = (hp + healing) if((hp + healing) < health) else health
        print(i, hp)
    return hp