def solution(s):
    number = dict()
    number['zero'] = 0
    number['one'] = 1
    number['two'] = 2
    number['three'] = 3 
    number['four'] = 4
    number['five'] = 5
    number['six'] = 6
    number['seven'] = 7
    number['eight'] = 8
    number['nine'] = 9
    # number 딕셔너리에 zero 부터 nine 까지 입력

    answer = ''
    eng = ''
    # answer = 정답용 문자열, eng = 영어 변환용 문자열

    for word in s:
        if word.isalpha():
            eng += word
            try:
                answer += str(number[eng])
                eng = ''
            except:
                None
            # 만일 word 가 영어라면 eng 에 추가, eng 가 number 의 키 값이라면 answer 에 value 값을 넣고 eng 초기화.
            # 그렇지 않다면 pass
        else:
            answer += word
            # word 가 숫자라면 answer 에 추가

    return int(answer)
    # 문자열인 answer 를 숫자로 변경

a = "one4seveneight"
print(solution(a))

# 다른사람의 풀이. 깔끔해서 가져왔다.
def solution(s):
    nums = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    # nums 딕셔너리에 값을 입력

    for key, value in nums.items():
        s = s.replace(key, value)
        # 딕셔너리 자료형의 .item() 함수를 사용.
        # s 의 영어 부분을 숫자로 변경
        
    return int(s)
    # 문자열인 s 를 숫자로 변경

a = "one4seveneight"
print(solution(a))