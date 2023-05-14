def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1], -x[0]))   # data 정렬

    lst = []                # 각 튜플의 나머지 합 저장 리스트
    for i in range(row_begin-1, row_end):   # 나머지 합 구하기
        total = 0
        for n in data[i]:
            total += n%(i+1)
        lst.append(total)
    
    ans = lst[0]            # 나머지 합끼리 비트연산 
    for n in lst[1:]:
        ans ^= n
    
    return ans
