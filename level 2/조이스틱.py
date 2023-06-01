def solution(name):
	# 조이스틱 조작 횟수 
    answer = 0
    
    # 기본 최소 좌우이동 횟수 = 길이 - 1
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
        # 해당 알파벳 변경횟수 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 해당 알파벳 다음이 A일 경우 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 아래 세 값 중 최소값으로 min_move 갱신
        # A. 기존 값
        # B. 연속된 A의 왼쪽시작 방식    (오른쪽으로 오다가 턴)
        # C. 연속된 A의 오른쪽시작 방식  (왼쪽으로 가다가 턴) 
        min_move = min([min_move, (2 * i + len(name) - next), (i + 2 * (len(name) -next))])
        
    # 알파벳 변경(상하이동) 횟수 + 좌우이동 횟수
    return answer + min_move
