def solution(numbers):
    answer = 0

    eng = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5',
           "six": '6', "seven": '7', "eight": '8', "nine": '9'}

    # replace() 문자열을 변경하는 함수
    for i in eng.keys():
        print(i)
        numbers = numbers.replace(i, eng[i])

    answer = int(numbers)

    return answer


numbers="onetwothreefourfivesixseveneightnine"
print(solution(numbers))