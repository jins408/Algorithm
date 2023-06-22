def solution(my_str, n):
    answer = []

    str_len = len(my_str)

    for i in range(0,str_len,n):
        # (i+n)인덱스 -> 슬라이싱은 범위가 초과되도 에러가 발생하지 않음
        a = my_str[i:i+n]
        answer.append(a)

    return answer
my_str ="abc1Addfggg4556b"
n = 6
print(solution(my_str, n))