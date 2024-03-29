def solution(K, words):
    # 여기에 코드를 작성해주세요.
    answer = 0

    temp = ''
    for word in words:
        if temp == '':
            temp = temp+word
        elif len(temp+word) >= K:
            answer += 1
            temp = word
        else:
            temp = temp+'_'+word

    if temp != '':
        answer += 1

    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")