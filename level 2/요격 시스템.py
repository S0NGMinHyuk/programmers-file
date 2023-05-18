def solution(targets):
    targets.sort()          # 미사일 오름차순 정렬
    ans = 0                 # 요격 미사일 개수
    end = targets[0][1]     # 첫 미사일의 끝 좌표

    # 다음 미사일이 요격 범위 안에 들어오면 요격 볌위 갱신,
    # 범위에 들어오지 않는다면 요격 미사일 추가 후 요격 범위 초기화.
    for target in targets[1:]:
        if target[0] < end:
            if target[1] < end:
                end = target[1]
        else:
            ans += 1
            end = target[1]

    # 마지막 요격 미사일 한 개 추가
    return ans + 1
