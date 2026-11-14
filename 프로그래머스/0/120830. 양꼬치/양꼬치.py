def solution(n, k):
    if n >= 10:
        juice = n // 10
        k = k - juice
    return n*12000+k*2000