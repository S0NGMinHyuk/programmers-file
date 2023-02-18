def solution(quiz):
    answer = []
    for q in quiz:
        a = q.split(" ")
        num = int(a[0])
        
        for i in range(1, len(a) - 2, 2):
            if a[i] == "+":
                num += int(a[i + 1])
            else:
                num -= int(a[i + 1])

        if num == int(a[-1]):
            answer.append("O")
        else:
            answer.append("X")
            
    return answer
