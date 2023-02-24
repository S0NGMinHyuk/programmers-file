def solution(my_string):
    a = []
    for i in my_string:
        if i not in a:
            a.append(i)
    return "".join(a)
