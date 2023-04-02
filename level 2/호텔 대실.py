def solution(book_time):
    room = []
    book_time.sort()
    for b in book_time:
        go, out = refineTime(b)
        # 방이 없는 경우 방 추가
        if room == []:
            room.append(out)
        else:
            for i in range(len(room)):
                # 이미 퇴실한 방일 경우 입실
                if room[i] <= go:
                    room[i] = out
                    break
            else:
                room.append(out)
                
    return len(room)


# 시간 문자열을 천의 자리 수로 변환하는 함수
def refineTime(time):
    go, out = time[0], time[1]
    go = int(go[:2]) * 100 + int(go[-2:])
    out = int(out[:2]) * 100 + int(out[-2:])
    
    # out 시간에 10분 추가
    if out % 100 >= 50:
        out += 50
    else:
        out += 10
    
    return go, out
