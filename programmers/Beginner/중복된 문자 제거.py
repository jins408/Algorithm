def solution(my_string):
    answer = ''

    for word in my_string:
        if word not in answer:
            answer += word
        

    return answer

my_string="We are the world"
print(solution(my_string))