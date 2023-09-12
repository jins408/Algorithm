def solution(numbers):
    answer = ''

    numbers = [str(i) for i in numbers]
    numbers.sort(reverse=True)
    print(numbers)


    #numbers.sort(key=lambda x: x*3, reverse=True)
    #print(numbers)

    for i in numbers:
        answer += i

    return str(int(answer))

numbers = [6, 10, 2]
    #[3, 30, 34, 5, 9]
    #[6, 10, 2]
print(solution(numbers))