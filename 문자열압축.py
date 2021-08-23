def solution(s):
    # 문자열 길이가 1이면 무조건 1을 반환한다.
    if len(s) == 1:
        return 1
    
    # 문자열 s의 길이 범위가 최대 1000이므로 answer는 1000에서 시작한다.
    answer = 1000

    # 문자열에 중복되는 문자의 길이는 최대가 문자열 길이의 절반이므로
    # 반복횟수도 문자열 길이의 절반만큼만 하면 된다.
    for length in range(1, len(s)//2 +1):
        start, cnt, end, plus = 0, 1, length, length
        
        # 압축된 문자열의 길이를 다룰 때 나머지 값을 계산하지 않으므로 나머지 값을 시작값으로 넣었다.
        change = len(s) % length 

        while 1:
            # 아직 문자열 길이를 초과하지 않을 경우
            if end <= len(s): # 문자열 비교
                if s[start:end] == s[start+plus:end+plus]:
                    cnt += 1

                    # 다음 문자열도 체크해야 함으로 plus에 length를 더해 체크할 수 있게 했다.
                    plus += length

                else: # 지금까지 체크한 문자열의 압축을 진행한다.
                    if cnt > 1:
                        change = change + length + len(str(cnt))
                        # cnt의 자릿수 길이가 필요하므로 str로 바꿨다가 len으로 숫자로 변환했다.
                    else:
                        change += length

                    # 다시 초기값 재설정
                    start += plus
                    end += plus
                    plus, cnt = length, 1

            else: # 문자열 길이에 따른 change값 비교, answer보다 작을 경우 교체했다.
                if change < answer:
                    answer = change

                # while 반복문 탈출    
                break 
    return answer