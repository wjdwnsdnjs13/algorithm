def solution(angle):
    return 1 if(angle//90 < 1) else 2 if(angle == 90) else 4 if(angle == 180) else 3