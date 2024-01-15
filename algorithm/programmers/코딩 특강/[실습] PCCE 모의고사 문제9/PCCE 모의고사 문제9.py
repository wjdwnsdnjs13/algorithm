def solution(num_list):
    answer = []
    for n in num_list:
        answer.append(calc(n))
    return answer

def calc(num):
    for i in range(2, int(num**0.5) + 1):
        if(num%i == 0): return False
    return True