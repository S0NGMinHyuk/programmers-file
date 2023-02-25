def solution(id_pw, db):
    comment = ""
    for i in db:
        if i[0] == id_pw[0]:     # id 일치
            if i[1] == id_pw[1]: # pw 일치
                comment = "login"
                break
            else:                # pw 불일치
                comment = "wrong pw"
                break
        else:                    # id 불일치
            comment = "fail"
    return comment
