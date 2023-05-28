def solution(genres, plays):
    theme = {} ; song = {}
    idx = 0
    for genre, play in zip(genres, plays):
        # theme 딕셔너리에 장르별 재생횟수 저장
        if genre not in theme:  # theme[genre]는 [재생횟수, 장르 이름] 형태
            theme[genre] = [play, genre]
        else:
            theme[genre][0] += play
        
        # song 딕셔너리에 장르별 가장 많이 재생된 곡 저장 (최대 2곡)
        if genre not in song:   # song에 genre가 없었으면 바로 idx 저장
            song[genre] = [idx]
        elif len(song[genre]) == 1: # song[gnere]의 요소가 1개면 idx 추가 후 정렬
            song[genre].append(idx)
            if plays[song[genre][0]] < plays[song[genre][1]]:
                song[genre][0], song[genre][1] = song[genre][1], song[genre][0]
        else:   # song[gnere]에 곡이 2개 있으면 가장 적은 재생횟수 곡 제거
            if play > plays[song[genre][0]]:
                song[genre][0], song[genre][1] = idx, song[genre][0]
            elif play > plays[song[genre][1]]:
                song[genre][1] = idx
            
        idx += 1    # 인덱스 증가

    order = sorted(theme.values(), key=lambda x:-x[0])  # 재생횟수 내림차순으로 정렬
    ans = []
    for i in order: # 재생횟수가 많은 장르 순으로 ans에 곡 추가
        ans += song[i[1]]
    return ans
