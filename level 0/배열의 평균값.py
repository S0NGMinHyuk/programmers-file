def solution(numbers):    # 내 풀이
    answer = 0
    for i in numbers:
        answer += i
    return answer / len(numbers)
    
   
def solution(numbers):    # 다른 사람의 풀이
    return sum(numbers) / len(numbers)   
