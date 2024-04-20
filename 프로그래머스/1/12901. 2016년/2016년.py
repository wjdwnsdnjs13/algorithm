def solution(a, b):
    import datetime

    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    answer = days[datetime.date(2016, a, b).weekday()]
    return answer