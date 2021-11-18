def solution(arr):
    answer = [0, 0]                  # 0번 인덱스 = 0의 개수, 1번 인덱스 = 1의 개수
    return compression(arr, answer)  # 재귀함수 호출

def compression(arr, answer):        # 재귀 함수, (compression = 압축)
    length = len(arr)
    temp = 0                         # temp = arr의 요소 총합
    for bundle in arr:
        temp += sum(bundle)
    
    if temp == 0:                    # temp가 0이면 arr 전체가 0
        answer[0] += 1               # answer의 0의 개수를 1 증가하고 answer 리턴
        return answer
    elif temp == length**2:          # temp가 length의 제곱이면 arr 전체가 1
        answer[1] += 1               # answer의 1의 개수를 1 증가하고 answer 리턴
        return answer
    else:                            # 그 외의 경우 arr를 각 사분면 별로 4등분 해 재귀함수 호출
        for num in range(4):
            row = int((num //2) *(length /2))      # row는 0, 0, length /2, length /2
            column = int((num %2) *(length /2))    # column는 0, length /2, 0, length /2
            next_arr = []

            for i in range(int(length/2)):         # next_arr에 4등분된 arr를 넣는 반복문
                next_arr.append(arr[row +i][column:column +int(length/2)])

            answer = compression(next_arr, answer) # 재귀함수 호출

        return answer                # answer 리턴


arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))                 # 정답 [4, 9]