def solution(lines): # 내 풀이
    l = sorted(lines, key=lambda x : (x[0], x[1]))
    order = [[0, 1], [0, 2], [1, 2]]
    gab = []

    for o in order:                  # gab에 겹치는 부분 추가
        if l[o[0]][1] > l[o[1]][0]:
            if l[o[0]][1] > l[o[1]][1]:
                gab.append([l[o[1]][0], l[o[1]][1]])
            else:
                gab.append([l[o[1]][0], l[o[0]][1]])
        else:
            gab.append([-101, -101])
    g = sorted(gab, key=lambda x : (x[0], x[1]))

    s, e, answer = -101, -101, 0     # 겹치는 부분 중 또 겹치는 부분 제외하고 총 길이 덧셈
    for i in g:
        if i:
            if i[0] >= e:
                answer += e - s
                s, e = i[0], i[1]
            else:
                if i[1] <= e:
                    continue
                else:
                    e = i[1]
    answer += e - s
    return answer



def solution(lines): # 다른사람의 풀이, respect
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))
    return len((s1 & s2) | (s2 & s3) | (s1 & s3)) 
