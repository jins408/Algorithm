s="one4seveneight"
def solution(s):
    answer = 0

    number = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5',
              "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    values_list = number.values()
    # dict_values(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    result = ''
    temp = ''

    for i, s in enumerate(s):
        if s in values_list: #숫자가 있으면 result에 추가
            result += s
        else:   # 숫자가 아니고 문자인 경우
            temp += s # temp 에 문자 한단어씩 추가
            if temp in number:  # temp가 number에 포함되어 있으면 ex) temp=one 인 경우
                result += number[temp] # number[one] one의 key 값의 value가 1이기 때문에 vvalue값을 result에 추가해준다
                temp = '' # temp 값 초기화 -> 초기화 시켜줘야 처음부터 다시 새로운 단어를 판단 할 수 있음
    return int(result)

print(solution(s))