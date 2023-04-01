def solution(babbling):
    say = ["aya", "ye", "woo", "ma"]
    cnt = 0
    # say 가 연속해서 있지 않는 경우 " " (띄어쓰기)로 변경
    for b in babbling:
        for s in say:
            if s*2 not in b and s in b:
                b = b.replace(s, " ")

        # 반복문 종료 후 띄어쓰기 제거
        b = b.replace(" ", "")

        # 발음할 수 있는 단어 조합일 경우 길이가 0이어야 한다.
        if len(b) == 0:
            cnt += 1

    return cnt 
