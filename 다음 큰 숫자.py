def solution(n):
    cnt = ten2two_count1(n) # n의 2진수 변환 시 1의 개수 저장
    while 1:
        n += 1
        target = ten2two_count1(n) 
        if cnt == target:
            return n

def ten2two_count1(num): # num을 2진수로 바꿨을 때 1의 개수 리턴하는 함수
    temp = []
    while num >= 2:
        moc, rest = divmod(num, 2)
        temp.append(rest) # 1의 개수가 필요한 것이므로 insert 대신 append 사용
        num = moc
    temp.append(num)

    return temp.count(1) # temp 내 1의 개수 리턴