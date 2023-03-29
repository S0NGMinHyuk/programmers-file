def solution(today, terms, privacies):
    td = today.split(".")
    td = [int(i) for i in td]
    term = {}
    for t in terms:
        a = t.split()
        term[a[0]] = int(a[1])
    
    result = []
    for o, p in enumerate(privacies):
        a = p.split()
        keeping = term[a[1]] # 보관기간간
        date = a[0].split(".")
        date = [int(i) for i in date]

        if date[2] > 1:
            date[2] -= 1
        else:
            date[2] = 28 ; date[1] -= 1
        
        date[1] += keeping
        if date[1] > 12:
            date[0] += date[1] // 12
            date[1] = date[1] % 12
            if date[1] == 0:
                date[1] = 12
                date[0] -= 1
        
        if td[0] > date[0]:
            result.append(o+1)
        elif td[0] == date[0] and td[1] > date[1]:
            result.append(o+1)
        elif td[0] == date[0] and td[1] == date[1] and td[2] > date[2]:
            result.append(o+1)
        else:
            None
        
    return result



td = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
p = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(td, terms, p))
