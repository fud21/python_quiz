import math
def solution(numer1, denom1, numer2, denom2):
    all_de = denom1*denom2
    all_num = numer1 * denom2 + numer2 * denom1
    # 최대공약수 함수
    gcd = math.gcd(all_num, all_de)
    all_num = all_num // gcd
    all_de = all_de // gcd
    
    answer = [all_num, all_de]
    return answer