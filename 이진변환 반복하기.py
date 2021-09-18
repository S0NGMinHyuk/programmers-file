def solution(s):
    cnt = 1 ; delete = 0
    while 1:
        s, delete = change(delete, s) # change 함수 무한 반복
        if len(s) == 1:
            return [cnt, delete]
            # len(s) == 1 은 s == '1' 이므로 cnt 와 delete 리턴
        cnt += 1

def change(delete, s): # 삭제된 0 개수 체크용 함수
    before = len(s)
    s = s.replace('0', '')
    after = len(s)
    delete += before -after # delete = 삭제한 0 의 개수
    return ten2two(s), delete # solution 함수에 ten2two() 의 리턴값과 증가된 delete 값 리턴

def ten2two(s): # 10진수 -> 2진수 변환용 함수
    num = len(s)
    save = []
    while 1:
        a = int(num / 2) ; b = int(num % 2)
        save.insert(0, str(b))
        if a != 0:
            num = a
        else:
            return "".join(save)

print(solution("110010101001"))