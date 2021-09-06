def deleteSharp(melody):
    # melody 문자열의 대문자# 을 소문자로 변환하는 함수
    while 1:
        if '#' in melody:
            sharp = melody.index('#')
            alphabet = melody[sharp -1]
            small = alphabet.lower()
            melody = melody.replace(alphabet+'#', small)
            # '#'의 인덱스를 찾아 그 앞자리 알파벳의 소문자로 변환
        else:
            return melody
            # melody 에 '#' 없으면 melody 리턴

def solution(m, musicinfos):
    song = '(None)' ; runTime = 0 ; m = deleteSharp(m)
    # 기본값 선언, m 문자열의 '#' 제거

    for i in musicinfos:
        info = list(i.split(','))
        time = (int(info[1][:2]) -int(info[0][:2])) *60 + (int(info[1][-2:]) -int(info[0][-2:]))
        melody = deleteSharp(info[3])
        # info = 곡 재생시간, 제목, 멜로디 정보 리스트, time = 재생시간(분)
        # melody 문자열의 '#' 제거

        while 1:
            if len(melody) < time:
                melody = melody *2
            else:
                melody = melody[:time]
                break
        # melody 문자열의 길이를 time 길이만큼 연장

        if m in melody:
            if time > runTime:
                song = info[2] ; runTime = time
        # m 이 melody 에 있으면 재생시간을 고려해 가장 긴 재생시간의 곡이면 song, runTime 값 변화
    
    return song

info = 	["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]
music = "CCB"

print(solution(music, info))