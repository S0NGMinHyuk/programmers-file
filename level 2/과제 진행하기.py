def solution(plans):
    # 정답 리스트, 과제 보관 리스트
    answer = []
    assign = []

    # plan 리스트 정제 (시간 순으로 정렬, 시작시간과 소요시간 숫자 자료형으로 변경)
    plans = sorted(plans, key=lambda x : x[1])
    for p in plans:
        p[1] = [int(p[1][:2]), int(p[1][-2:])]
        p[2] = int(p[2])


    for i, now in enumerate(plans):
        # 마지막 인덱스가 아닌 경우
        try: 
            next = plans[i + 1]
            time_gap = (next[1][0] - now[1][0]) * 60 + (next[1][1] - now[1][1])
            # 과제 소요시간이 시간차이보다 작을 경우
            if time_gap >= now[2]:
                time_gap -= now[2]
                answer.append(now[0])
                # 밀린 과제가 있을 경우
                if assign:
                    for _ in range(len(assign)):
                        # 시간차이가 밀린 과제 소요시간보다 크거나 같은 경우 과제 완료
                        if assign[-1][2] <= time_gap:
                            time_gap -= assign[-1][2]
                            answer.append(assign.pop()[0])
                        # 밀린 과제 소요시간이 더 큰 경우 시간차만큼 감소
                        else:
                            assign[-1][2] -= time_gap
                            break
            # 과제 소요시간이 시간차이보다 크거나 같은 경우
            else:
                now[2] -= time_gap
                assign.append(now)
        # 마지막 인덱스인 경우
        except: 
            answer.append(now[0])
            # 밀린 과제 순서대로 완료
            for _ in range(len(assign)):
                answer.append(assign.pop()[0])

    return answer
