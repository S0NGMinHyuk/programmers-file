def solution(num, total):
    answer = [None] * num
    if num % 2 == 1:    # num 이 홀수인 경우
        answer[num//2] = total // num
        for i in range(1, num//2 + 1):
            answer[num//2 + i], answer[num//2 - i] = answer[num//2] + i, answer[num//2] - i
            
    else:               # num 이 짝수인 경우
        answer[num//2], answer[num//2 - 1] = total // num + 1, total // num
        for i in range(1, (num-2)//2 + 1):
            answer[num//2 + i], answer[num//2 - 1 - i] = total // num + 1 + i, total // num - i
    return answer
