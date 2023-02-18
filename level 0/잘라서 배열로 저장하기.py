def solution(my_str, n):
    answer = [None] * ((len(my_str) - 1) // n + 1)

    for i in range(0, len(answer)):
        answer[i] = my_str[i*n:(i+1)*n]     # 슬라이싱은 인덱스 초과 에러가 생기지 않는다.
        
    return answer
