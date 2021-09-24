def solution(skill, skill_trees):
    answer = 0 # 정답용 변수
    
    for tree in skill_trees: # tree = 배울 스킬 순서
        wrong_tree = False
        c_skill = list(skill)
        # wrong_tree = 스킬트리 순서가 맞는지 저장하는 변수
        # c_skill = skill 의 리스트 자료형

        for target in tree: # target = 지금 배울 스킬
            if target in c_skill:
                for i in range(len(c_skill)):
                    if c_skill[i] == 0:
                        None # 이미 배운 스킬은 패스
                    elif c_skill[i] == target:
                        c_skill[i] = 0
                        break
                        # 배워야 할 스킬이 target 과 같으면 해당 스킬(c_skill[i])을 0으로 변경
                    else:
                        wrong_tree = True
                        break
                        # 스킬 트리 순서에 맞지 않으므로 wrong_tree 를 1로 바꾸고 break
            if wrong_tree:
                break # 스킬 트리 순서에 맞지 않으므로 break
        else:
            answer += 1 # 스킬 트리에 맞는 순서이므로 answer 에 1 증가
    return answer

skill = "CBD"
tree = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, tree))