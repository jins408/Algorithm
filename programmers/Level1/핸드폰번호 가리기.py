def solution(phone_number):
    answer = ''

    a = phone_number[:-4]

    for i in a:
        if i in phone_number:
            answer += "*"

    return answer + phone_number[-4:]


phone_number = "01033334444"
print(solution(phone_number))