def solution(scores):
    student, answer = len(scores), ""
    n_score = list(map(list, zip(*scores)))
    # student = 학생 수, answer = 학점 문자열, n_score = scores 리스트의 행렬 변환
    # 이후 평균을 구하는 과정에서 학생 수를 계속 구해야 함, len 함수를 한 번만 쓰기 위해 미리 선언

    for i, point in enumerate(n_score):
        me, c_student, total = point[i], student, sum(point)
        point.sort()
        # me = 내가 나에게 준 점수, c_student = 평균 구할 때 분모(제수, divisor)가 될 값

        if len(point) == 2:
            c_student -= 1
            # point 의 요소가 2개뿐이면 어떤 경우든 total 에서 me 값을 뺀 값이 평균이다.

        elif me == point[0] or me == point[-1]:
            if me == point[1] or me == point[-2]:
                me = 0
                # me 의 점수가 유일한 최대, 최소값이 아니라면 0으로 변경
            else:
                c_student -= 1
                # me 의 값이 유일한 최대, 최소값이면 분모값을 1 감소
        else:
            # "me 의 점수가 최대, 최소 값이 아니라면" 의 경우
            me = 0

        aver = (total -me) / c_student
        # aver = 점수의 평균값

        if aver >= 90:
            answer += "A"
        elif aver >= 80:
            answer += "B"
        elif aver >= 70:
            answer += "C"
        elif aver >= 50:
            answer += "D"
        else:
            answer += "F"
        # aver 에 따라 학점을 answer 에 추가
        
    return answer

a = [[50,90],[50,87]]
print(solution(a))