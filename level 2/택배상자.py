def solution(order):
    # 스택 알고리즘 사용
    stack = []
    cnt, index = 0, 0

    for i in range(1, len(order) + 1):
        # 상자를 실을 순서일 경우
        if i == order[index]:
            cnt += 1
            index += 1
            while (stack and stack[-1] == order[index]):
                stack.pop()
                cnt += 1
                index += 1
        # 아직 상자를 실을 순서가 아닐 경우
        elif i < order[index]:
            stack.append(i)
        # 반복문 종료 조건 (컨테이너 상자를 실을 차례 X, 스택의 상자도 다 체크한 경우)
        else:
            return cnt
        
    # 상자를 다 실었을 경우
    return cnt
