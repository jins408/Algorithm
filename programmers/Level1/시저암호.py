def solution(s, n):
    s = list(s)

    for i in range(len(s)):
        if s[i].isupper():
            # s[i]의 아스키 코드 값을 구하고 'a'의 아스키 코드를 빼고 이동시킬 만큼 n을 더한다.
            # 알파벳이 25글자이니 더 큰 수인 26으로 나머지 연산자를 이용하면 z의 경우처럼 맨 마지막이 다시 처음으로 돌아가는 경우의 수를 해결할 수 있음
            # 다시 'a'의 아스키 코드 값을 더하면 원하는 소문자의 아스키 코드 값을 구할 수 있음
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        if s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    # join() 함수를 사용하여 리스트를 문자열로 바꿈
    return "".join(s)