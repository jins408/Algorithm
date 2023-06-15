def solution(num_list):
    answer = []

    num = len(num_list)
    #for i in range(1, num+1):
    #    answer.append(num_list[num-i])

    for i in range(len(num_list)-1, -1,-1):
        print(num_list[i])

    return answer




num_list = [1,2,3,4,5]
print(solution(num_list))