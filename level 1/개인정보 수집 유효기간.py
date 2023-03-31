def solution(today, terms, privacies):
    # today 데이터 정제
    td = today.split(".")
    td = [int(i) for i in td]

    # 약관 유효기간 딕셔너리 생성
    term = {}
    for t in terms:
        a = t.split()
        term[a[0]] = int(a[1])
    
    result = []
    for o, p in enumerate(privacies):
        a = p.split()
        keeping = term[a[1]] # 보관기간

        # date 변수 생성 및 정제
        date = a[0].split(".")
        date = [int(i) for i in date]

        # date 의 날짜를 하루 전으로 변경
        if date[2] > 1:
            date[2] -= 1
        else:
            date[2] = 28 ; date[1] -= 1 
            # keeping 이 1 이상이기 때문에 date[1]이 0이어도 상관없다.
        
        # date 의 달을 keeping 만큼 증가
        date[1] += keeping
        if date[1] > 12:
            date[0] += date[1] // 12
            date[1] = date[1] % 12
            # date[1]이 0일 경우 예외처리
            if date[1] == 0:
                date[1] = 12
                date[0] -= 1
        
        # 오늘 날짜와 비교 후 result 리스트에 추가 or 스킵
        if td[0] > date[0]:
            result.append(o+1)
        elif td[0] == date[0] and td[1] > date[1]:
            result.append(o+1)
        elif td[0] == date[0] and td[1] == date[1] and td[2] > date[2]:
            result.append(o+1)
        else:
            None
        
    return result



td = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
p = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(td, terms, p))
