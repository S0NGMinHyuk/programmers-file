def solution(polynomial):
    p = polynomial.replace(" + ", " ").split()  # 항 리스트 생성
    x = 0 ; n = 0                               # x = x 계수, n = 정수
    for i in p:
        try:
            n += int(i)                         # 정수 추가
        except:
            if i == "x":
                i = "0x" ; x += 1
            i = list(i)
            x += int("".join(i[:-1]))           # x 계수 추가
    
    answer = ""
    if x > 1:
        answer = str(x) + "x"
    elif x == 1:
        answer = "x"
    

    if answer:
        if n:
            answer = answer + " + " + str(n)
        else:
            return answer
    elif n:
        answer = str(n)
    else:
        answer ="0"

    return answer
