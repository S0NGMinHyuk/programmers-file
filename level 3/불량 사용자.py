def solution(user_id, banned_id):
    # 밴 아이디 조건마다 해당하는 아이디 저장
    banList = [[] for _ in range(len(banned_id))]
    for i, ban in enumerate(banned_id):
        for user in user_id:
            if len(ban) == len(user):
                for a, b in zip(ban, user):
                    if a == "*" or a == b:
                        continue
                    else:
                        break
                else:
                    banList[i].append(user)

    # 밴 아이디로 만들 수 있는 모든 조합 생성
    from itertools import product
    availableIds = list(product(*banList))
    
    resultIds = set()
    for id in availableIds:
        if len(id) == len(set(id)):     # 조합에 중복값 확인
            id = "".join(sorted(id))    # sort 후 문자열로 바꿔서 이미 resultIds에 있는지 확인
            if id not in resultIds:
                resultIds.add(id)

    return len(resultIds)
