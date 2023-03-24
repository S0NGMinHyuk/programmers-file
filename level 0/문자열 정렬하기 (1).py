def solution(my_string):
    num = []
    for i in my_string:
        if i.isdigit():
            num.append(int(i))
    return sorted(num)
