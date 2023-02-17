def solution(babbling):  # 내 풀이
    answer = 0
    for word in babbling:
        if word[0] == "a" and len(word) >= 3:    # aya 탐색
            if word[1] == "y":
                if word[2] == "a":
                    if len(word) != 3:
                        babbling.append(word[3:])
                        continue
                    else:
                        answer += 1
                else:
                    None
            else:
                None        
        elif word[0] == "y" and len(word) >= 2:   # ye 탐색
            if word[1] == "e":
                if len(word) != 2:
                    babbling.append(word[2:])
                    continue
                else:
                    answer += 1
            else:
                None
        elif word[0] == "w" and len(word) >= 3:    # woo 탐색
            if word[1] == "o":
                if word[2] == "o":
                    if len(word) != 3:
                        babbling.append(word[3:])
                        continue
                    else:
                        answer += 1
                else:
                    None
            else:
                None 
        elif word[0] == "m" and len(word) >= 2:     # ma 탐색
            if word[1] == "a":
                if len(word) != 2:
                    babbling.append(word[2:])
                    continue
                else:
                    answer += 1
            else:
                None
        else:
            None
    return answer


a = ["aya", "yee", "u", "maa", "wyeoo"]
print(solution(a))


def solution(babbling): # 다른 사람의 풀이
    answer = 0
    for b in babbling:
        for p in ["aya", "ye", "woo", "ma"]:
            b = b.replace(p, " ")
        if len(b.strip()) == 0:
            answer += 1
    return answer


b = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
print(solution(b))