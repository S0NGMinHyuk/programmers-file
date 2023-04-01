def solution(id_list, report, k):
    dic = {}
    for i in id_list:
        # [신고당한 횟수, 내가 신고한 유저, 받은 메일 수]
        dic[i] = [0, [], 0]
    
    for r in report:
        # a = 신고자, b = 신고당한 사람
        a, b = r.split()
        # 중복신고 방지 (report 리스트를 set 자료형으로 변경하는 방법도 있다)
        if a not in dic[b][1]:
            dic[b][1].append(a)
            dic[b][0] += 1
        else:
            None
    
    # k회 이상 신고당할 경우 신고자의 받은 메일 값 증가
    for user in id_list:
        if dic[user][0] >= k:
            for i in dic[user][1]:
                dic[i][2] += 1

    # dic의 밸류 리스트에서 필요한 값만 추출
    return [i[2] for i in dic.values()]
