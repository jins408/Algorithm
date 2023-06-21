def solution(my_string):
    answer = 0

    a = my_string.split(" ")
    num = int(a[0])
    for i in range(1, len(a)):
        if a[i] == "+":
            num += int(a[i+1])
        elif a[i] == "-":
            num -= int(a[i+1])

    answer = num
    return answer

my_string = "3 + 4"
print(solution(my_string))