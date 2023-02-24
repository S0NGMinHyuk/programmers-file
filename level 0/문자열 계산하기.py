def solution(my_string):
    ms = my_string.split()
    num = [int(ms[i]) for i in range(0, len(ms), 2)]   # 숫자만 있는 리스트 생성
    print(num)
    
    ind = 0
    for i in range(1, len(ms), 2):
        ind += 1
        if ms[i] == "+":
            num[0] += num[ind]
        else:
            num[0] -= num[ind]
            
    return num[0]
