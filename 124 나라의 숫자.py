def solution(n):
    temp = [] # 10진수를 124로 변환하기 위한 임시 리스트

    while n > 3:
        moc, rest = divmod(n, 3)
        if rest == 0:
            rest = 3 ; moc -= 1 # 나머지가 0일 경우 몫에서 1 줄이고 나머지를 3으로 변경
        temp.insert(0, rest) # temp 에 나머지를 맨 앞에 인서트
        n = moc
    temp.insert(0, n) # while 문 종료 후 temp 에 n 삽입

    change = '' # 정답용 문자열

    for i in temp:
        if i == 1:
            change += '1'
        elif i == 2:
            change += '2'
        elif i == 3:
            change += '4' # i 가 3일 경우 4로 변경

    return change