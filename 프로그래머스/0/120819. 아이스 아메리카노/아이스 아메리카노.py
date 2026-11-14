def solution(money):
    count = money // 5500
    change = money % 5500
    answer = [count, change]
    return answer