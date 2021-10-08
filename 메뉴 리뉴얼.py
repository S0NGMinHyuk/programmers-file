from itertools import combinations

def solution(orders, course):
    answer = [] # 정답용 리스트

    for c in course: # c = 메뉴 갯수
        dict = {} 

        for o in orders: # o = 주문 조합
            if len(o) >= c:
                o = list(sorted(o)) # combinations 를 쓰기 위해 리스트로 변경
                combi = list(combinations(o, c)) # combinations 함수를 통해 가능한 모든 조합 추출

                for k in combi:
                    k = "".join(k) # combinations 는 튜플로 반환하기 때문에 문자열로 변환
                    if k not in dict:
                        dict[k] = 1
                    else:
                        dict[k] += 1
        else:
            if len(dict) == 0: # 모든 o가 c보다 작을 때
                continue
    
        temp = []
        times = max(dict.values())
        if times == 1: # times가 1이라면 중복된 조합이 없는 경우
            continue
    
        for i in dict.keys():
            if dict[i] == times:
                temp.append(i)

        answer += temp # answer에 temp 추가

    return sorted(answer) # 오름차순으로 정렬


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))