def solution(weights):
    mans = dict()        # 사람 몸무게 딕셔너리
    ans = 0             # 정답 변수

    # 각 몸무게가 몇 명인지 딕셔너리에 한 명씩 추가
    for i in weights:
        if i not in mans:
            mans[i] = 1
        else:
            mans[i] += 1
        
        # 자기 앞 순서에 시소 짝꿍 몸무게가 있는지, 
        # 있다면 몇 명이 있는지 ans에 추가가
        for x in [2, 1/2, 3/2, 2/3, 4/3, 3/4]:
            if (i * x) in mans:
                ans += mans[i * x]
        # 자기 몸무게와 같은 사람 수 추가 (본인 제외)
        ans += mans[i] - 1
    
    return ans
