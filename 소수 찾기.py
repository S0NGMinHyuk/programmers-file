from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(numbers) # permutations를 쓰기 위해 리스트로 변경
    done = [] # 중복된 값을 반복하지 않기 위한 리스트

    for i in range(1, len(numbers) +1):
        combi = list(permutations(numbers, i)) # numbers의 값 조합을 i개 만큼 조합
        for num in combi:
            num = int("".join(num)) # combi 값은 튜플 속 문자열이므로 숫자로 변경
            if num not in done:
                if num <= 1: # num이 0이나 1일 경우
                    continue
                done.append(num)
                check = check_prime(num)
                if check: # num이 소수인 경우
                    answer += 1
            else: # num이 이미 done에 있다면
                continue

    return answer

def check_prime(n): # n이 소수인지 판별하는 함수, 소수면 1, 아니면 0을 리턴한다.
    for i in range(2, n):
        if n % i == 0:
            return 0
    else:
        return 1

print(solution("011")) # 정답 2