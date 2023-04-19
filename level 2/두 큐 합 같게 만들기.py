def solution(queue1, queue2):
    ai, bi = 0, 0                     # q1 인덱스, q2 인덱스
    ans, length = 0, len(queue1)      # 정답 변수, q1의 길이
    a, b = sum(queue1), sum(queue2)   # q1의 총합, q2의 총합

    # 더 큰 큐에선 인덱스만 늘리고, 작은 큐에는 뒤에 값 추가
    while a != b:
        if a > b:              
            a -= queue1[ai]
            b += queue1[ai]
            queue2.append(queue1[ai])
            ai += 1
        else:
            a += queue2[bi]
            queue1.append(queue2[bi])
            b -= queue2[bi]
            bi += 1
        ans += 1
        
        # 각 큐의 원소값을 같게 할 수 없는 경우
        if ans > (length * 3):
            return -1
        
    return ans
