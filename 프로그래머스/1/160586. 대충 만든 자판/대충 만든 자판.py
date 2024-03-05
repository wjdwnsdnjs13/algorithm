def solution(keymap, targets):
    answer = []
    
    for target in targets:
        count = 0
        flag = False
        for t in target:
            tmp = 99999
            for key in keymap:
                k = list(key)
                if(t in k):
                    tmp = min(tmp, k.index(t) + 1)
            if(tmp == 99999): flag = True
            count += tmp
        answer.append(-1 if(flag) else count)
            
    
    return answer