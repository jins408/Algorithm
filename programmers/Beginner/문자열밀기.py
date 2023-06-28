# word함수 A를 오른쪽으로 한칸 씩 밀어줌
def word(A):
    a = ''
    # 단어의 제일 끝글자가 가장 앞으로 와야해서 먼저 for문을 돌려 맨뒷글자를 맨앞으로 a(빈문자열)넣어줌
    for i in range(len(A)):
        if i == len(A) - 1:
            a += A[i]
    # 맨끝 글자를 제외하고 a 문자열에 넣어준다.
    for i in range(len(A) - 1):
        a += A[i]

    return a

def solution(A, B):
    cnt = 0
    # A와 B가 동일하면 오른쪽을 밀 필요가 없음
    if A == B:
        return 0
    else:
        # A와 B가 같지 않으면 같아질 때 까지 while문 돌림
        while True:
            # 오른쪽 한칸씩 이동하는 함수
            temp = word(A)
            # 밀린 횟수를 return 받아야해서 cnt 증가시켜줌
            cnt += 1
            A = temp
            # A와 B같으면 break걸려서 cnt(밀린횟수) return해줌
            if A == B:
                break
            # 오른쪽으로 문자를 밀었지만, B와 동일한게 없을 경우 -1
            # cnt로 밀어버린 수와 원래 단어가 길이 같아지면 A를 한바퀴 다 돌았다고 본다.
            elif cnt >= len(A) and A == temp:
                return -1
            else:
                # A와 B가 같아 질 때까지 함수를 계속 타도록 해줌
                word(A)

        return cnt

A ="hello"
B ="elloh"
print(solution(A,B))