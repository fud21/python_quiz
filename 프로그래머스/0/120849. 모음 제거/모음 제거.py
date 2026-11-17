def solution(my_string):
    # 제거는 replace("")
    remove = 'aeiou'
    for i in remove:
        my_string = my_string.replace(i, "")
    return my_string