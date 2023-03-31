def solution(s):
    result = 0

    while 1:
        # while 무한루프 탈출 조건 1
        if len(s) <= 1:
            result += len(s)
            break
        
        # x와 그 외 알파벳 개수 확인
        x = s[0] ; s = s[1:]
        cnt_x = 1 ; cnt_else = 0
        for i, a in enumerate(s):
            if a == x:
                cnt_x += 1
            else:
                cnt_else += 1
                # 둘의 개수가 같을 경우 for 문 탈출
                if cnt_x == cnt_else:
                    result += 1
                    s = s[i+1:]
                    break
        # for 문을 끝까지 돌 경우는 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없는 경우.
        # while 무한루프를 탈출하며 코드를 마쳐야 한다.
        else:
            result += 1
            break

    return result
