def solution(numbers, target):
    # 깊이 우선 탐색 재귀함수 호출
    return dfs(numbers, target, len(numbers) - 1, 0, 0, 0)


def dfs(numbers, target, l, index, total, ans):
    # 마지막 인덱스가 아닐 경우
    if index < l:
        for i in [1, -1]:
            # 인덱스 값을 더하기 and 빼기 후
            # temp 값을 기반으로 다음 인덱스로 재귀함수 호출
            temp = total + numbers[index] * i
            ans = dfs(numbers, target, l, index + 1, temp, ans)

    # 마지막 인덱스일 경우
    else:
        # 마지막 인덱스 값을 더하거나 뺀 값이 target과 같을 경우 ans값 1 증가 후 리턴
        if (total + numbers[index] == target) or (total - numbers[index] == target):
            ans += 1
        return ans
    
    # dfs 재귀함수가 끝나고 최종 ans값 리턴
    return ans
