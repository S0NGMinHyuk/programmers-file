def solution(my_string):
    answer = 0
    m = my_string.lower()
    
    eng = "abcdefghijklmnopqrstuvwxyz"
    for i in eng:
        m = m.replace(i, " ")
    
    m = m.split()
    for i in m:
        answer += int(i)
    return answer
