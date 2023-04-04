def solution(picks, minerals):
    dia = [] ; iron = [] ; stone = []
    for slicing in range(sum(picks)):
        m = minerals[slicing * 5:slicing * 5 + 5]
        for i in range(len(m)):
            if m[i] == "diamond":
                m[i] = 25
            elif m[i] == "iron":
                m[i] = 5
            else:
                m[i] = 1
        if m:
            dia.append(len(m))
            stone.append(sum(m))
            temp = 0
            for i in m:
                if i == 1:
                    temp += 1
                else:
                    temp += i//5
            iron.append(temp)
        else:
            break
    
    if len(dia) < sum(picks):
        skip = sum(picks) - len(dia)
        for i in range(2, 0, -1):
            if picks[i] and skip:
                if picks[i] >= skip:
                    picks[i] -= skip
                    skip = 0
                else:
                    skip -= picks[i]
                    picks[i] = 0
            else:
                None
    

    dic = { 0:stone, 1:iron, 2:dia }
    answer = 0
    for i, num in enumerate(reversed(picks)):
        for _ in range(num):
            temp = min(dic[i])
            ind = dic[i].index(temp)
            dia[ind] = iron[ind] = stone[ind] = 126
            answer += temp
    return answer
