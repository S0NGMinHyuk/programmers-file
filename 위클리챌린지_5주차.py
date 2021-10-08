def solution(word):
    answer = 0
    temp = 'AEIOU' # 문자를 숫자(index)로 바꾸기 위한 임시 문자열

    for i, num in enumerate(word):
        if i == 0:
            answer += temp.index(num) *781 +1
        elif i == 1:
            answer += temp.index(num) *156 +1
        elif i == 2:
            answer += temp.index(num) *31 +1
        elif i == 3:
            answer += temp.index(num) *6 +1
        else: # i == 4
            answer += temp.index(num) +1
    # 각각의 경우를 계산해보니 규칙이 있다.

    return answer

word = "EIO"
print(solution(word)) # 정답 1189