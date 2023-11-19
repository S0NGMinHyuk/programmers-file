def solution(n, costs):
    # 크루스칼 알고리즘 사용

    answer = 0
    unions = [None] * n             # 각 섬마다 연결된 조합 표시
    costs.sort(key=lambda x:x[2])   # 다리건설비용을 기준으로 정렬

    group = 1   # 조합 번호
    for a, b, cost in costs:
        if unions[a] == None and unions[b] == None:     # 둘 다 고립된 섬일 경우 조합 생성
            unions[a] = group ; unions[b] = group
            answer += cost
            group += 1
        elif unions[a] == None and unions[b] != None:   # a 혹은 b가 연결된 섬이 있을 경우 조합에 추가
            unions[a] = unions[b]
            answer += cost
        elif unions[a] != None and unions[b] == None:   # a 혹은 b가 연결된 섬이 있을 경우 조합에 추가
            unions[b] = unions[a]
            answer += cost
        elif unions[a] == unions[b]:                    # 두 섬이 이미 같은 조합에 있을 경우 패스 (건설비용 추가 X)
            continue
        else:
            temp = [unions[a], unions[b]]               # 두 섬이 다른 조합에 있을 경우 조합번호 통일
            for i in range(len(unions)):
                if unions[i] == temp[1]:
                    unions[i] = temp[0]
            answer += cost
        
    return answer


n, costs = 	5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]
print(solution(n, costs))
