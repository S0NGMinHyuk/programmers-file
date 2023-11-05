def solution(arr):
    minIndex = arr.index(min(arr))  # 최솟값의 인덱스
    result = 1                      # 끝까지 살아남는 숫자 갯수, 1은 최솟값

    # 최솟값의 왼쪽부터 탐색
    # 자신의 왼쪽 값들보다 작으면 생존
    index = 0
    low = None
    while index < minIndex:
        if low == None or low > arr[index]:
            result += 1
            low = arr[index]
        index += 1
    
    # 최솟값의 오른쪽부터 탐색
    # 자신의 오른쪽 값들보다 작으면 생존
    index = len(arr) -1
    low = None
    while index > minIndex:
        if low == None or low > arr[index]:
            result += 1
            low = arr[index]
        index -= 1
    
    return result
  
