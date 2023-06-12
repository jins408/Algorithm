# Fraction 모듈로 기약분수 구하기
'''
from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    answer = []
    den = denom1 * denom2
    numer1 *= denom2
    numer2 *= denom1
    num = numer1 + numer2

    result = Fraction(num, den)
    answer.append(result.denominator)
    answer.append(result.numerator)

    return answer
'''

# 2로 나눴을 때, 더이상 나눌 수 없을때까지 계산해서 기약분수 구하기
def solution(numer1, denom1, numer2, denom2):

    den = denom1 * denom2  #공통분모
    numer1 *= denom2
    numer2 *= denom1
    num = numer1 + numer2  #분자값 = 분자 * 분모
    cnt = 2

    while cnt <= den: # cnt가 공통분모 값이랑 동잃할때 까지 while문 돌림
        if num%cnt == 0 and den%cnt == 0:  # 2로 나눈 나머지 값이 0일때까지 나눔(기약분수 구하기 위해)
            num = num//cnt
            den = den//cnt
            cnt = 2
            continue
        cnt+=1 #2가 아닌 다른 값으로도 나눴을때, 나머지가 0일 수 있으므로 cnt값을 +1
    return [num, den]

numer1=1
denom1=2
numer2=3
denom2=4
print(solution(numer1, denom1, numer2, denom2))