def solution(msg):
    answer = [] # 정답용 리스트
    word = '' ; temp = '' # msg 에서 값을 받을 문자열 변수
    index = 0 ; check = 1 # msg 의 인덱스와 while 문 내 조건문에 필요한 check 값
    english = list('@ABCDEFGHIJKLMNOPQRSTUVWXYZ') 
    # 영어 알파벳 리스트, answer 에 추가될 때 인덱스 값을 맞추기 위해 맨 앞에 트래쉬값 @ 추가

    while 1:
        try:
            if check:
                word = msg[index]
                temp = word +msg[index +1]
            else:
                word = temp
                temp = word +msg[index +1]
                check = 1 # check 초기화
            # check 에 따라 word 의 값이 달라짐
        except:
            answer.append(english.index(word))
            break
            # 마지막 값인 경우 위의 try 코드 내 temp 값을 넣는 줄에서 오류가 발생
            # answer 리스트에 word 의 인덱스를 넣고 while 문 탈출

        if temp not in english:
            english.append(temp)
            answer.append(english.index(word))
            # temp 가 english 에 없다면 english 에 temp 를 추가하고 answer 리스트에 englist 내 word 값의 인덱스 추가
        else:
            check = 0
            # temp 가 english 에 있다면 check 를 0으로 변경해 위의 코드에서 word 값을 현재 temp 값으로 변경

        index += 1 # for 문이 아니기 때문에 index 를 마지막에 1 증가

    return answer


# 테스트케이스
msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))
# 정답
print('[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]')