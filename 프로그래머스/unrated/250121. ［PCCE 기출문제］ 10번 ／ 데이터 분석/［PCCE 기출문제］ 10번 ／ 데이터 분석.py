def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    # data =  ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]
# ext : 어떤 기준인지
# val_ext : 뽑아낼 정보의 기준값을 나타내는 정수
# sort_by : 정보를 정렬할 기준이 되는 문자열
# data에서 ext의 값이 val_ext보다 작은 데이터만 뽑아서 sort_by에 해당하는 값을 기준으로 오름차순 정렬해서 리턴
    criteria = {"code" : 0, "date" : 1, "maximum" : 2, "remain" : 3}
    answer = [d for d in data if val_ext > d[criteria[ext]]]
    answer.sort(key=lambda x: x[criteria[sort_by]])
    return answer