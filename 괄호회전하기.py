def solution(s):
    result = 0 # 정답용 변수
    for _ in range(len(s)):
        target = s[_:] + s[:_] # 문자열을 왼쪽으로 돌려 변환하는 코드.
        answer = check(target)
        result += answer
    return result

def check(target):
    # 스택 알고리즘 사용
    stack = [] 
    right = ["[", "{", "("] 
    for i in target:
        if i in right: 
            # i 가 right 에 있는 문자라면 무조건 stack 에 추가
            stack.append(i)
        else:
            # i 가 right 에 없는 상태에서 stack 이 비어있다면 return 0
            if len(stack) == 0:
                return 0
            else:
                # i 가 stack[-1]과 페어를 이루지 않는다면 무조건 올바르지 않은 문자열이기 때문에
                # 페어를 이룬다면 pop, 그렇지 않다면 return 0
                if (i == "]" and stack[-1] != "[") or (i == "}" and stack[-1] != "{") or (i == ")" and stack[-1] != "("):
                    return 0
                else:
                    stack.pop()

    if len(stack) == 0:
        return 1 # 무사히 append와 pop를 지나 stack이 비어있다면 올바른 문자열
    else:
        return 0 # 그렇지 않다면 올바르지 않은 문자열 (예시->"[[[[")


s = "[](){}"
print(solution(s))