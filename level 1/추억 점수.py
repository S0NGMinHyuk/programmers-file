def solution(name, yearning, photo):
    # 사람 별 그리움 점수 딕셔너리 생성
    man = {}
    for n, y in zip(name, yearning):
        man[n] = y
    
    result = []
    for p in photo:
        score = 0
        for i in p:
            if i in man:
                score += man[i]
            else:
                None
        result.append(score)

    return result
