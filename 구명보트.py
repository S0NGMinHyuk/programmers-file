def solution(people, limit):
    people.sort(reverse=True)
    # people 리스트를 무거운 사람 순으로 정렬
    boat, front, back = 0, 0, len(people) -1
    # boat = 보트 갯수, front = 앞 인덱스, back = 뒤 인덱스
    while (front <= back):
        # front 가 back 보다 크면 반복문 탈출할 것
        if people[front] <= limit / 2:
            # 가장 무거운 사람이 limit 의 절반이면 무조건 두 명씩 탈 수 있음
            boat += ((back -front) // 2) +1
            break
            # 남은 사람 수에 대한 보트 개수를 추가하고 반복문 탈출

        elif people[front] + people[back] <= limit:
            # 가장 무거운 사람과 가장 가벼운 사람의 무게 합이 limit 이하면 두 명씩 탈 수 있음
            back -= 1 # b뒤 인덱스 앞당김

        front += 1 # 앞 인덱스 키움
        boat += 1  # 보트 개수 추가

    return boat

    # 처음 풀었던 답안. 정확도 검사는 통과했지만 pop을 사용해 효율성 검사를 통과 못함

    # people.sort()
    # boat = 0
    # while len(people):
    #     first = people.pop()
    #     try:
    #         if limit -first >= people[0]:
    #             people.pop(0)
    #         boat += 1
    #     except:
    #         boat += 1
    # return boat