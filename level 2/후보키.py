from itertools import combinations

def find(candidate):    # 유일성을 만족하는 열의 조합 찾기
    keys = []   # 유일성을 가지는 인덱스 조합 리스트
    idx = [i for i in range(len(candidate))]
    
    for k in range(2, len(candidate)+1):
        for lst in combinations(idx, k):    # k개만큼 인덱스 조합 생성
            reverse = list(zip(*[candidate[i] for i in lst]))   # lst의 인덱스끼리 새로운 조합 생성
            
            if len(reverse) != len(set(reverse)):   # 새로 만든 조합이 유일성을 만족하지 못할 경우
                continue
            
            for key in keys:
                if set(key).issubset(lst):  # 유일성은 만족하지만 최소성을 만족하지 못할 경우 break
                    break
            else:
                keys.append(lst)    # 유일성과 최소성을 만족하는 인덱스 조합일 경우 keys에 추가
                
    return len(keys)    # 유일성, 최소성을 만족하는 인덱스 조합 개수 리턴


def solution(relations):
    answer = 0
    relations = list(zip(*relations))   # 전치행렬로 변환
    candidate = []      # 유일성을 만족하지 못하는 열
    
    for element in relations:
        if len(element) == len(set(element)):   # 유일성을 만족하는 열일 경우
            answer += 1
        else:
            candidate.append(element)   # 유일성을 만족하지 못하는 열 리스트
    
    answer += find(candidate)
    
    return answer
