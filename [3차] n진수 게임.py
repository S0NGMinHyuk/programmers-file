def solution(n, t, m, p):              # n: 진법, t: 구할 숫자 개수, m: 참가 인원, p: 튜브 순서
    answer = ''
    num = 0                            # 시작 숫자
    total = []                         # 모든 사람이 말하는 숫자 리스트
    while len(total) < m*t:            # total의 길이가 m*t 이상이면 튜브가 말할 t개의 개수가 충족
        changeNum = ten2n(num, n)      # 정수인 num을 n진수로 변환
        total += changeNum             # 변환한 리스트를 total에 추가
        num += 1                       # num 1 증가
    for i in range(0, t):
        answer += total[p-1+m*i]       # total에서 튜브가 말할 숫자만 answer에 추가

    return answer


def ten2n(num, n):                     # 정수인 num을 n진수로 표현한 리스트로 변환
    temp = []
    while num >= n:                    # num이 n보다 크거나 같을 때
        moc, rest = divmod(num, n)
        num = moc                      # 몫은 재사용, 나머지는 temp에 인서트
        rest = changeNum(rest)         # 10진수 이상일 경우 알파벳으로 바꿔야 하기 때문에 변환
        temp.insert(0, rest)         
    else:
        num = changeNum(num)           # 마지막으로 num 값도 변환 후 temp에 인서트
        temp.insert(0, num)
    return temp


def changeNum(i):                      # 10진수 이상일 경우 나머지를 알파벳으로 변환하는 함수
    temp = "ABCDEF"
    if i <= 9:                         # 나머지가 한 자릿수면 문자열로 바꿔서 리턴
        return str(i)
    else:                              # 나머지가 두 자릿수일 경우
        return temp[i-10]              # 나머지에 맞는 알파벳을 리턴 


n, t, m, p = 16,16,2,2
print(solution(n,t,m,p))               # 정답 13579BDF01234567