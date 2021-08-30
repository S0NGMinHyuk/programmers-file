def solution(price, money, count):
    result = ((count*(count +1)) //2) *price -money
    if result < 0:
        return 0
    else:
        return result