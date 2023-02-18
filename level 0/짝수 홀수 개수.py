def solution(num_list):
    cnt = 0
    for i in num_list:
        if i % 2 == 0:
            cnt += 1
    return [cnt, len(num_list) - cnt]
