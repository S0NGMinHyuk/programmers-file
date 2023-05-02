def solution(numbers):
    ans = []    # 정답 리스트
    for num in numbers:
        # num을 2진수 리스트로 변환
        binary = ten_to_binary(num)

        if len(binary) == sum(binary):    # 2진수의 모든 원소가 1일 경우
            binary.append(1)
            binary[1] = 0
        else:                             # 2진수의 원소 중 0이 있을 경우
            idx_0 = 0                     # 가장 마지막 0 값과
            idx_1 = None                  # 마지막 0 뒤 최초의 1 값 변경

            for i in range(len(binary)):  # 마지막 0 인덱스 탐색
                if binary[i] == 0 and i > idx_0:
                    idx_0 = i
  
            for i in range(idx_0 + 1, len(binary)):  # 0 다음 최초의 1 인덱스 탐색
                if binary[i] == 1:
                    idx_1 = i
                    break
            if idx_1:                     # 마지막 0 다음에 1이 있는 경우
                binary[idx_0], binary[idx_1] = binary[idx_1], binary[idx_0]
            else:                         # 0이 마지막 인덱스인 경우
                binary[idx_0] = 1
        
        ans.append(binary_to_ten(binary[::-1]))      # 2진수 리스트를 10진수 숫자로 변환
    
    return ans


# 10진수 -> 2진수 리스트 변환
def ten_to_binary(num):
    ans = []
    while num >= 2:
        num, rest = divmod(num, 2)
        ans.append(rest)
    ans.append(num)
    return ans[::-1]


# 뒤집어진 2진수 리스트 -> 10진수 값 변환
def binary_to_ten(array):
    ans = 0
    for i, num in enumerate(array):
        ans += num * 2**i
    return ans


n = [1001,337,0,1,333,673,343,221,898,997,121,1015,665,779,891,421,222,256,512,128,100]
print(solution(n))
print([1002, 338, 1, 2, 334, 674, 347, 222, 899, 998, 122, 1019, 666, 781, 893, 422, 223, 257, 513, 129, 101])  # 
