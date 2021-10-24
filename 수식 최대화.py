def solution(expression):
    answer = 0 ; temp = 0
    # 가능한 연산자 조합 6가지
    orders = ['+-*', '+*-', '-*+', '-+*', '*+-', '*-+']  
    exp = []                 # expression을 숫자와 연산자를 나눈 리스트
    for c in expression:
        try:                 # c가 숫자라면 temp에 자릿수대로 추가
            c = int(c)                
            temp *= 10
            temp += c                 
        except:              # c가 연산자라면 exp에 temp와 c 추가
            exp.append(temp)
            exp.append(c)
            temp = 0
    else:
        exp.append(temp)     # 마지막으로 exp에 temp 추가
    
    for order in orders:
        result = calculate(exp, order) # calculate 함수 실행
        
        if result > answer:  # result가 answer보다 크면 값 교체
            answer = result

    return answer

def calculate(exp, order):
    for o in order:
        stack = [] ; check = False
        for i in range(len(exp)):
            if o == exp[i]:           # exp[i]가 목표 연산자일 경우
                temp = stack.pop()    # stack의 마지막 값 pop
                temp2 = exp[i+1]      #exp[i+1]의 값을 끌어오기

                if exp[i] == '+':     # exp[i]의 연산자에 따라 계산 후 stack에 추가
                    stack.append(temp+temp2)
                elif exp[i] == '-':
                    stack.append(temp-temp2)
                elif exp[i] == '*':
                    stack.append(temp*temp2)
                check = True          # exp[i+1]의 경우를 스킵해야 하므로 check 변경

            elif check:               # exp[i+1]의 경우를 스킵하며 check 원상복구
                check = False

            else:                     # exp[i]가 계산할 연산자가 아닐 경우 stack에 추가
                stack.append(exp[i])
        else:
            exp = stack               # exp를 stack으로 교체, 목표 연산자를 계산한 리스트

    if stack[0] < 0:                  # 결과값이 음수면 양수로 교체
        return stack[0] * -1
    else:
        return stack[0]

e = "100-200*300-500+20"
print(solution(e))