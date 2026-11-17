import math
def solution(numbers):
    # max보다는 sort로
    numbers.sort(reverse=True)
    a = numbers[0]
    b = numbers[1]
    
    return a*b