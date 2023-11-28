def solution(data, ext, val_ext, sort_by):
    answer = []

    indexCode = {
        "code" : 0, 
        "date" : 1, 
        "maximum" : 2, 
        "remain" : 3
    }

    # data에서 ext 값이 val_ext보다 작은 데이터 추출
    for info in data:
        if info[indexCode[ext]] < val_ext:
            answer.append(info)
    
    # sort_by에 해당하는 값을 기준으로 오름차순으로 정렬
    return sorted(answer, key=lambda x:x[indexCode[sort_by]])
