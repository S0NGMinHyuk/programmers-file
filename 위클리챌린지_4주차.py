def solution(table, languages, preference):
    result = '' ; point = 0
    # result = 정답용 문자열, point = 점수 확인용 리스트

    for job in table:
        job = list(job.split()) ; total = 0
        # 문자열인 job 변수를 리스트로 변환
        # total = 해당 직업군의 언어 총합 점수

        for i in range(len(languages)):
            try:
                total += (6 -job.index(languages[i])) *preference[i]
                # languages[i]가 job 리스트에 있다면 total 점수에 추가
            except:
                None
                # 없다면 0점이므로 None

        if total > point:
            point = total ; result = job[0]
            # total 이 point 보다 크다면 result 에 직업의 이름을 넣고
            # point 값을 total 값으로 교환

        elif total == point:
            if job[0] < result: 
                result = job[0]
            # total 값이 point 값과 같다면 직업의 이름이 사전 순에서
            # 더 먼저 오는 값으로 교환, point 값은 건드릴 필요 없다.
            
    return result

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
print(solution(table, languages, preference))