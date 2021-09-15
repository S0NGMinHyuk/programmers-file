def solution(enter, leave):
    answer = [0] *len(enter) ; room = [] ; out = 0
    # answer = 정답용 리스트 , room = 회의실 역할 리스트, out = leave 리스트의 인덱스 역할 변수

    for come in enter:
        room.append(come) # 우선 room 에 사람을 입장
        if len(room) > 1:
            people = len(room) -1
            # room 에 둘 이상 있을 경우, people = 내부 사람 수 -1 

            for man in room:
                if answer[man -1] < people:
                    answer[man -1] = people
                else:
                    answer[man -1] += 1
            # people 이 room 안에 있는 사람이 그동안 만난 사람 수보다 크다면 people 을 대입
            # 그렇지 않다면 이번에 들어온 사람을 새롭게 만난 사람에게 1 증가

        try:
            while leave[out] in room:
                room.remove(leave[out])
                out += 1
                # leave 리스트의 순서대로 room 에서 퇴장
        except:
            return answer 
        # 마지막은 out 의 범위가 len(leave) 를 벗어나므로 에러나 남, except 문에서 answer 를 리턴

enter = [1,4,2,3]
leave = [2,1,4,3]
print(solution(enter, leave))