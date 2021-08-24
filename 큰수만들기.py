def solution(number, k):
    # stack에 입력값을 순서대로 삽입 
    stack = [number[0]]
    for num in number[1:]:
        # 들어오는 값이 stack 값보다 크면, 기존의 값을 제거하고 새로운 값으로 바꿈 
        # 참고 : len(stack) > 0 == stack
        while len(stack) > 0 and stack[-1] < num and k > 0:
            # 값을 한개 빼서 k는 1이 제거 
            k -= 1
            # 내부의 값을 제거 
            stack.pop()
        
        # while 문 조건이 맞지 않을 경우 새로운 값을 삽입 
        stack.append(num)

    # 만일 충분히 제거하지 못했으면 남은 부분은 단순하게 삭제
    # 이렇게 해도 되는 이유는 이미 큰 수부터 앞에서 채워넣었기 때문 
    if k != 0:
        stack = stack[:-k]
    
    return ''.join(stack)

#--------------------------------------------------------------------------------------

def solution(number, k):
    # 넘버 문자열을 리스트로 변환
    number = list(number)

    # 만일 한가지 숫자로만 이뤄진 경우 빠르게 반환 (테스트케이스 10번용 but 실패)
    if len(set(number)) == 1:  
        return number[0]*(len(number)-k)

    # 최대값을 시작할 첫 번째 자릿수를 정하기 위한 코드
    big = "0"
    for i in range(k):
        # 만일 9가 나오면 이하 내용 스킵
        if number[i] == "9":
            number = number[i:]
            k -= i
            break
        elif number[i] > big:
            big, index = number[i], i
    else:
        # for 문을 다 돌고 난 후 정리
        number = number[index:]
        k -= index
    
    # 남은 k 값만큼 작은 수를 없애기 위한 코드
    start = 0
    while k:
        for i in range(start, len(number)):
            try:
                if number[i] < number[i+1]:
                    number.pop(i)
                    k -= 1
                    # 이미 반복한 코드를 다시 반복하기 않기 위해 사용
                    start = i -1
                    break
                else:
                    None
            except:
                # k 가 남았을 경우 맨 뒷 자리부터 k 만큼 삭제
                number = number[:-k]
                k = 0
                break
    
    return "".join(number)