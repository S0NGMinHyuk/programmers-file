def solution(emergency):
    temp = list(emergency)          # 리스트 완전 복사
    temp.sort(reverse=True)
    order = {}                      # 우선도 딕셔너리 생성

    for i, n in enumerate(temp):
        order[n] = i + 1            # 응급도 별 순서 지정

    for i in range(len(emergency)):
        emergency[i] = order[emergency[i]]

    return emergency
