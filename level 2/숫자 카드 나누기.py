def solution(arrayA, arrayB):
    # 각 배열의 최대공약수 계산
    gcdA, gcdB = get_gcd(arrayA), get_gcd(arrayB)
    
    # 공약수가 1이 아닐 경우, 상대 배열에서 체크
    gcdA = check_num(gcdA, arrayB) if gcdA else 0
    gcdB = check_num(gcdB, arrayA) if gcdB else 0
    
    # 두 값 중 더 큰 수 리턴
    return gcdA if gcdA > gcdB else gcdB


def get_gcd(array):
    from math import gcd
    
    ans = array[0]
    for num in array[1:]:
        ans = gcd(ans, num)
        if ans == 1:
            return 0
    return ans


def check_num(num, array):
    for n in array:
        if n % num == 0: 
            return 0
    return num
