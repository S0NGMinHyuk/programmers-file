def solution(my_string):
    delete = ["a", "e", "i", "o", "u"]
    for i in delete:
        my_string = my_string.replace(i, "")
    return my_string
