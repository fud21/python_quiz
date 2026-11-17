def solution(babbling):
    answer = 0
    for word in babbling:
        for ok in ['aya', 'ye', 'woo', 'ma']:
            word = word.replace(ok, " ")
            # 공백으로 바꿈
            # 공백 제거했을 때 문자 안 남으면! 
        if word. strip() == "": # 제거한 거 == ""
            answer += 1 # 갯수 카운트
    return answer