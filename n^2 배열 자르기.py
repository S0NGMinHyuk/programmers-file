def solution(n, left, right):                   # 극한의 메모리 관리 문제
    answer = []
    for i in range(1, n+1):
        if left > n:                            # left가 n보다 클 경우 만들 필요가 없는 값이므로
            left -= n ; right -= n              # left와 right 값을 n만큼 줄이고 스킵
            continue

        temp = [i]*i                            # 배열 초반 같은 값이 연속되는 부분은 
        answer += temp                          # for문 없이 따로 생성 후 추가
        answer += [c for c in range(i+1, n+1)]  # 뒷부분 연속값만 for문으로 생성 후 추가

        if len(answer) >= right+1:              # answer 값이 right+1보다 많으면 
            break                               # 이후 값은 필요 없는 값이므로 반복문 탈출

    return answer[left:right+1]                 # answer 값 중 필요한 값만 리턴

print(solution(4, 7, 14))