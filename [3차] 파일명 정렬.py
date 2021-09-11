def solution(files):
    answer = []
    # 파일의 정보가 담길 answer 리스트

    for index, data in enumerate(files):
        check = True 
        # 나중에 TAIL 부분을 검사할 때 필요

        for i, word in enumerate(data):
            if word in '0123456789':
                if check:
                    HEAD = data[:i]
                    NUMBERstart = i
                    check = False
                else:
                    None
            # word 가 숫자이고 check 가 True 라면 맨 처음 만난 숫자이므로 이전의 부분이 HEAD 임을 알 수 있고 
            # i 값이 NUMBER 부분의 시작인덱스이므로 NUMBERStart 에 저장, check 를 False 로 변경
            # word 가 숫자이지만 check 가 False 라면 스킵
            else:
                if check == False:
                    NUMBER = data[NUMBERstart:i]
                    TAIL = data[i:]
                    answer.append([HEAD, HEAD.upper(), NUMBER, int(NUMBER), TAIL, index])
                    break
                else:
                    None
            # word 가 숫자가 아니지만 check 가 True 라면 아직 HEAD 부분이므로 스킵
            # word 가 숫자가 아니고 check 가 False 라면 TAIL 부분의 시작이므로 이전까지의 부분이 NUMBER 부분이므로 
            # NUMBER, TAIL 의 부분을 완성하고 answer 리스트에 추가
            # 이후 sort 과정에 필요한 HEAD.upper(), int(NUMBER), index 를 함께 추가
        else:
            answer.append([HEAD, HEAD.upper(), data[NUMBERstart:], int(data[NUMBERstart:]), '', index])
            # TAIL 부분이 공백이라면 20~27번 코드를 실행하지 않음.
            # 따로 for-else 문을 사용해 직접 answer 리스트에 추가, TAIL 이 공백이기 때문에 TAIL 부분을'' 로 변경
    else:
        answer.sort(key=lambda x : (x[1], x[3], x[5]))
        return [i[0] +i[2] +i[4] for i in answer]
        # answer 리스트에 추가된 요소의 1, 3, 5 번 인덱스만 따져서 sort.
        # 이후 필요한 부분인 0, 2, 4 번 인덱스의 문자열만 붙여 리스트로 만든 후 리턴

# 예제
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))
# 정답
print('["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]')