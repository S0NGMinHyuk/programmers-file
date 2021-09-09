def solution(weights, head2head):
    detail = [] ; index = 1
    # detail = 각 선수 별 정보 리스트를 담을 리스트
    # index = 선수 번호
    for man, record in zip(weights, head2head):
        win = game = advertage = 0
        # win = 승리 수, game = 게임 수, advertage = 몸무게 불리한 게임 승리 수

        for enemy, match in enumerate(record):
            if match == 'W':
                game += 1 ; win += 1
                if man < weights[enemy]:
                    advertage += 1
            elif match == 'L':
                game += 1
        # 이겼을 경우 game, win 을 1 증가 & 상대 몸무게보다 가벼울 경우 advertage 도 1 증가
        # 졌을 경우 game 만 1 증가, N 일 경우는 스킵

        try:
            detail.append([index, man, win/game, advertage])
        except:
            detail.append([index, man, 0, advertage])
        # detail 에 선수의 정보(번호, 몸무게, 승률, 불리게임 이긴 수)를 추가
        # game = 0 일 경우 에러가 나므로 try-except 문으로 예외처리

        index += 1
        # 선수 번호 1 증가
    
    detail.sort(key=lambda x : (-x[2], -x[3], -x[1], x[0]))
    # 승률, 불리게임 이긴 수, 몸무게, 번호 순으로 내림, 오름 차순을 사용해 sort

    return [i[0] for i in detail]
    # sort 된 detail 리스트 내 요소의 0번째 인덱스인 선수 번호만 리턴


weight = [50,82,75,120]
head = ["NLWL","WNLL","LWNW","WWLN"]
print(solution(weight, head))