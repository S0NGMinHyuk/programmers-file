def solution(n, wires):
    plant = dict()
    for wire in wires:
        # 양 뱡향에 대해 송전탑 전력망 연결
        plant = put_a_to_b(plant, wire[0], wire[1])
        plant = put_a_to_b(plant, wire[1], wire[0])

    gap = n    # 송전탑 개수 차이 변수
    for cut in wires:
        # 가장 적은 개수 차이 구하기
        a = get_plants(plant, cut[0], cut[1])
        b = get_plants(plant, cut[1], cut[0])

        if a < b:
            a, b = b, a
        gap = (a-b) if (a-b) < gap else gap

    return gap


# a와 b 사이 전력망 연결 함수
def put_a_to_b(plant, a, b):
    if a not in plant:
        plant[a] = [a, b]
    else:
        plant[a].append(b)
    return plant


# a와 b 사이 전력망이 끊겼을 때 a와 이어진 송전탑 개수 리턴 함수
def get_plants(plant, a, b):
    tower = list(plant[a])                      # a와 연결된 송전탑 리스트

    idx = 0
    while idx < len(tower):
        if tower[idx] == a or tower[idx] == b:  # 자기 자신과 끊긴 b 송전탑은 제외
            idx += 1
        else:                                   # 이어진 송전탑에서 또 이어진 송전탑 추가
            for n in plant[tower[idx]]:
                if n not in tower:
                    tower.append(n)
            idx += 1

    return len(tower) - 1                       # b를 제외한 송전탑 개수 리턴


n, wires = 7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]
print(solution(n, wires))
