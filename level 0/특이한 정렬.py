def solution(numlist, n):
    for i in range(len(numlist)):               # 람다식 사용을 위해 데이터 변형
        numlist[i] = [numlist[i], abs(n - numlist[i])]
    
    numlist.sort(key=lambda x : (x[1], -x[0]))  # 정렬
    
    return [i[0] for i in numlist]              # 데이터 형태 원상복구
