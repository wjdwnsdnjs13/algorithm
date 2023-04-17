def solution(phone_book):
    answer = True
    phone = set(phone_book)
    for p in phone_book:
        for i in range(len(p) - 1):
            if p[:i + 1] in phone:
                return False
    return True