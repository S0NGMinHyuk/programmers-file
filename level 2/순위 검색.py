from bisect import bisect_left  # 이진탐색용 라이브러리 사용

def solution(info, query):  # 내 풀이
    mans = dict()
    for detail in info:     # mans에 info의 모든 경우의 key값 정리
        detail = detail.split()
        score = int(detail.pop())
        mans = update_mans(mans, detail, score, 0)
    
    for k in mans:  # mans 딕셔너리의 score 정렬
        mans[k].sort()
    
    ans = []
    for q in query:     # query 요구에 따른 사람의 수를 ans에 추가
        q = q.split()   # q를 필요한 형태로 가공
        score = int(q.pop())
        q = q[::2]
        str_q = "".join(q)

        if str_q in mans:   # 이진탐색을 통해 score 이상의 사람 수 탐색
            ans.append(len(mans[str_q]) - bisect_left(mans[str_q], score))
        else:
            ans.append(0)
    
    return ans


def update_mans(mans, detail, score, index):    # index의 값과 index의 값이 "-"일 경우를 mans에 추가
    if index > 3:
        str_detail = "".join(detail)    # 마지막 인덱스를 넘었을 경우 mans에 추가
        try:
            mans[str_detail].append(score)
        except:
            mans[str_detail] = [score]
    
        return mans
    
    if detail[index] != "-":    # index 값이 있다면 현재 값과 "-"인 경우 2가지로 나눠서 진행
        temp = list(detail)
        temp[index] = "-"
        update_mans(mans, detail, score, index+1)
        update_mans(mans, temp, score, index+1)
    else:   # index 값이 "-"인 경우 나누지 않고 진행
        update_mans(mans, detail, score, index+1)
    
    return mans



info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))


# ______________________________________________________________________________________________________________


from bisect import bisect_left
from itertools import combinations


def solution(info, query):
    info_dict = {}

    for i in range(len(info)):
        infol = info[i].split()
        value = infol[:-1]
        score = infol[-1]

        for i in range(5):  # combinations 함수를 통해 각각의 요소 조합을 만들어 info_dict에 추가
            for c in combinations(value, i):
                temp = "".join(c)
                if temp in info_dict:
                    info_dict[temp].append(int(score))
                else:
                    info_dict[temp] = [int(score)]

    for k in info_dict:
        info_dict[k].sort()  # dict안의 조합들을 점수순으로 정렬
    # sort를 하려면 for문을 따로 떼서 sort만 해야하는 것 같다. 다른 for문에서 sort를 하면 시간초과가 난다.
    
    ans = []
    for qu in query:
        myqu = qu.split()   # qu_key, qu_score를 만들고 가공
        qu_score = myqu[-1]
        qu_key = myqu[:-1]

        while 'and' in qu_key:
            qu_key.remove('and')
        while '-' in qu_key:
            qu_key.remove('-')
        qu_key = "".join(qu_key)

        if qu_key in info_dict: # score를 넘는 사람의 수를 ans에 추가
            scores = info_dict[qu_key]
            ans.append(len(scores) - bisect_left(scores, int(qu_score)))
        else:
            ans.append(0)
    
    return ans

# ______________________________________________________________________________________________________________

def solution(info, query):
    # 미리 data에 모든 경우에 따른 key 값 생성
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())

    # info 값에 따른 모든 경우의 key값에 점수 추가
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    # data 내부 점수 정렬
    for k in data:
        data[k].sort()
    # sort를 하려면 for문을 따로 떼서 sort만 해야하는 것 같다. 다른 for문에서 sort를 하면 시간초과가 난다.

    # query 값을 조건 pool과 점수 find로 분리
    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])

        # pool에서 find 이진탐색
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
        answer.append(len(pool)-l)

    return answer
