def solution(s):
    every = []
    double = []
    for i in s:
        if i not in every:
            every.append(i)
        else:
            double.append(i)
    a = sorted(list(set(every)-set(double)))
    return "".join(a)  
