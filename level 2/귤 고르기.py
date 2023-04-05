def solution(k, tangerine):
    # size 딕셔너리에 귤 크기별 개수 저장
    size = {}
    for t in tangerine:
        if t not in size:
            size[t] = 1
        else:
            size[t] += 1
    
    # 같은 크기의 귤 개수를 내림차순으로 정렬
    v = sorted(size.values(), reverse=True)

    # 가장 종류가 많은 귤부터 상자에 채워넣으며 종류 return
    for i in range(len(v)):
        if v[i] >= k:
            return i + 1
        else:
            k -= v[i]
