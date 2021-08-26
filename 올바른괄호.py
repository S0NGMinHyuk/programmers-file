def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            elif stack[-1] == "(":
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

s = "()()"
print(solution(s))