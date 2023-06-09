def solution(s):
    # 이진 변환 횟수를 기록하는 변수 선언
    change = 0
    # 0 제거 개수
    zero = 0

    while s != '1': # 1만 남을때까지 과정을 반복
        change += 1 # 반복횟수 증가
        num = ""  # '0'을 제거하고 1만 남은 문자얼 넣을 변수
        for word in s:
            if word != '0':
                num += word # num = 111111
        s2 = len(num)  # num문자일 길이
        zero += len(s) - s2 # 전체길이-num문자열길이빼면 0을 제거한 개수
        s = bin(s2)[2:] # bin()이진변환 함수 0b110이라서 앞의두자리 잘라줘서 -> s = 110

    return [change, zero]



s ="110010101001"
print(solution(s))