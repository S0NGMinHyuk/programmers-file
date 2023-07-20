def solution(begin, target, words):
    # deque 모듈 사용
    from collections import deque
    
    
    used = {begin}              # q에 중복값이 쌓이지 않기 위해 체크 (시간복잡도를 위해 set 사용)
    q = deque([[begin, 0]])     # DFS 알고리즘을 위한 큐 생성 <- [현재 단어, 거친 단계]
    
    while q:
        temp = q.popleft()

        # target 값이 될 경우 종료
        if temp[0] == target: return temp[1]    

        # 현재 단어 다음 단계의 단어를 words에서 탐색 후 q에 추가
        for word in words:
            if word not in used:
                if compareWords(temp[0], word):
                    q.append([word, temp[1]+1])
                    used.add(word)
    
    # while 문을 탈출하는 경우는 target을 만들지 못하는 경우
    return 0


# w1과 w2가 한 가지 알파벳만 다른지 판별하는 함수 (한 가지 알파벳만 다르면 True, 아니면 False 리턴)
def compareWords(w1, w2):
    diff = 1
    for a, b in zip(w1, w2):
        if a != b:
            diff -= 1
            if diff < 0:
                return False
    return True
