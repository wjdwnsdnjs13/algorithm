def solution(nums):
    if len(nums)/2<len(set(nums)):
        answer = len(nums)/2
    else:
        answer = len(set(nums))
    return answer