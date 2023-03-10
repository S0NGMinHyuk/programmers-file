def solution(spell, dic):
    spell = set(spell)
    for d in dic:

        setD = set(d)
        if spell & setD == spell:
            lenD = len(d)
            for i in spell:
                d = d.replace(i, "")
            if len(d) - lenD == -len(spell):
                return 1
    
    return 2
