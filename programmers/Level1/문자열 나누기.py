def solution(s):
    answer = 0

    # 첫문자 가 a라고 하면 읽으면서 a의 개수를 카운트하고 a와 다른 문자를 합산(!!)해서 카운트 합니다.
    # 문자마다 각각 세는게 아님 b가 두번 c가 두번 나오면 다른 글자들이 나온 횟수는 4가 되는거임
    cnt = 0 # 첫문자와 같은 글자를 카운트해줄 변수
    sum = 0 # 첫문와 다른 글자들을 카운트해줄 변수
    a = '' # 쪼갠 문자열을 담은 변수
    first = 0 # 비교할 첫문자
    for i in range(len(s)):
        if s[i] == s[first]:
            cnt += 1
        else:
            sum += 1
        if cnt == sum:
            # i인덱스로 계속 비교해 나가기 때문에 i+1(i는0부터)까지 문자열 분리
            a += s[first:i+1]+","
            first += cnt+sum # 비교할 첫문자가 바뀌어야 하기때문에 cnt+sum을 해준다.
            # 첫문자와 비교가 끝나면 다시 카운트를 해줘야하기때문에 변수 초기화
            cnt = 0
            sum = 0
        if cnt != sum and i == len(s)-1: # 카운트수가 다르거나, 더이상 셀 문자열이 없는거까지 문자열 분리
            a += s[first:i+1]+","

    #print(a)
    a = a.split(',')
    a = a[:-1]
    #print(a)
    answer = len(a)

    return answer
s= "abracadabra"
    #"banana"
    #"abracadabra"
    #"aaabbaccccabba"
print(solution(s))