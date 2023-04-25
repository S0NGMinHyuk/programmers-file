def solution(cards):
    boxes = []                  # 상자 그룹 리스트
    visit = [0] * len(cards)    # 열어본 상자인지 확인하는 리스트
    idx = 0                     # 상자 그룹 시작 인덱스
    
    # 모든 상자를 열어보지 않았을 경우
    while sum(visit) < len(cards):
        # 상자 그룹 시작 인덱스 도출
        while visit[idx] == 1:
            idx += 1

        # idx번 상자부터 열어보며 상자 그룹 생성
        i = idx
        cnt = 0
        while visit[i] == 0:
            visit[i] = 1
            i = cards[i] - 1
            cnt += 1
        boxes.append(cnt)
    
    # 상자 그룹 내림차순 정렬
    boxes.sort(reverse=True)

    # 최고 점수 리턴 / 상자 그룹이 1개일 경우 0 리턴
    return boxes[0] * boxes[1] if len(boxes) > 1 else 0
