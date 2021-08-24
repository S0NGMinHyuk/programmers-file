def solution(orders, course):
    menus = []
    for ord in orders:
        menus.append(set(ord))

    answer = []
    for i in range(len(menus) -1):
        for j in range(i+1, len(menus)):
            same = menus[i] & menus[j]
            if len(same) in course:
                same = "".join(sorted(list(same)))
                if same not in answer:
                    answer.append(same)
    
    return answer