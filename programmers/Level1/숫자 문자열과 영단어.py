s="one4seveneight"
def solution(s):
    answer = 0

    number = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5',
              "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    values_list = number.values()
    result = ''
    temp = ''

    for i, s in enumerate(s):
        if s in values_list:
            result += s
        else:
            temp += s
            if temp in number:
                result += number[temp]
                temp = ''
    return int(result)

print(solution(s))