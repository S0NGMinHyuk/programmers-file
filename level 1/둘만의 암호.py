def solution(s, skip, index):
    # skip을 제외한 영어 알파벳 문자열 생성
    eng = "abcdefghijklmnopqrstuvwxyz"
    for e in skip:
        eng = eng.replace(e, "")

    answer = ""
    for i in range(len(s)):
        si = eng.index(s[i])
        si += index
        # eng 범위 초과 시 정제 작업
        if si >= len(eng):
            si = si % len(eng)
        answer += eng[si]
    
    return answer
