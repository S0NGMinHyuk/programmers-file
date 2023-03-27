def solution(n, m, section):
    # 칠하는 횟수
    cnt = 0
    
    while len(section) > 0:
        a = section[0]
        for i in range(1, m + 1):
            # section 인덱스 오류 방지
            try:
                if (section[i] - a) >= m:
                    cnt += 1
                    section = section[i:]
                    break
            # 오류 시 맨 마지막이라는 뜻 (종료)
            except:
                cnt += 1
                section = []
                break
    return cnt
