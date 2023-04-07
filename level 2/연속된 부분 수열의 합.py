def solution(sequence, k):
    #누적합, 수열 길이, 수열 길이 저장 변수, 답
    plus, cnt, length, answer = 0, 0, 1000001, None

    # 마지막 값을 더할 때 답이 나오는 경우를 위해 리스트 가공
    sequence.append(0)
    
    for i, num in enumerate(sequence):
        # 수열 길이가 1인 경우
        if num == k:
            return [i, i]
        
        # num을 더하기 전 plus가 k와 같으면 수열 길이에 따라 answer 값 변경 or 유지
        if plus == k:
            if cnt < length:
                length = cnt
                answer = [i - cnt, i - 1]

        # 수열 증가, 수열 길이 증가
        plus += num
        cnt += 1

        # 누적합이 k보다 크면 k보다 작거나 같아질 때까지 수열 맨 앞 값부터 감소
        if plus > k:
            while plus > k:
                plus -= sequence[i - cnt + 1]
                cnt -= 1
        else:
            continue
    
    return answer
