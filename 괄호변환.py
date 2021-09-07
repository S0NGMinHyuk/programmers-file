def check(sentence):
    # sentence 문자열 속 균형 잡힌 문자열의 끝 인덱스를 알기 위한 함수
    cnt = 0 ; start = sentence[0] ; index = 0
    for i in sentence:
        index += 1
        if i == start:
            cnt += 1
            if cnt == 0:
                return index
        else:
            cnt -= 1
            if cnt == 0:
                return index
    # cnt = 0 -> 균형잡힌 문자열이라는 뜻이므로 해당 문자의 index 를 리턴

def balance(sentence):
    # sentence 문자열이 올바른 괄호 문자열인지 검사하는 함수 / stack 알고리즘 사용
    stack = []
    for i in sentence:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            elif stack[-1] == "(":
                stack.pop()
            else:
                return False
    return True
    # 올바른 괄호 문자열이면 True 를 리턴, 그렇지 않다면 False 를 리턴

def solution(sentence):
    if sentence == '':
        return sentence
    # 만일 sentence 가 빈 문자열이라면 sentence 리턴

    i = check(sentence)
    uuu = sentence[:i] ; vvv = sentence[i:]
    # check 함수를 통해 균형잡힌 문자열의 끝 인덱스를 받고 uuu, vvv 로 분리

    if balance(uuu):
        vvv = solution(vvv)
        return uuu +vvv
        # uuu 가 올바른 괄호 문자열이면 vvv 문자열에 대해서 재귀적으로 수행하고 해당 값을 uuu 의 뒤에 붙여 리턴
    else:
        uuu = uuu[1:-1]
        uuu_change = ''
        for k in uuu:
            if k == '(':
                uuu_change += ')'
            else:
                uuu_change += '('
        vvv = solution(vvv)
        return '(' +vvv +')' +uuu_change
        # uuu 가 올바른 괄호 문자열이 아니라면 uuu의 맨 앞, 뒤 괄호를 떼고 나머지 괄호의 방향을 뒤집어야 하므로
        # uuu_change 라는 문자열에 반복문을 사용해 뒤집은 값을 저장
        # vvv 문자열에 대해서도 재귀적으로 수행하고 이후 문제 설명대로 문자열들을 붙여 리턴


p = "()))((()"
print(solution(p))