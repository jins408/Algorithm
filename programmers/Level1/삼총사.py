def solution(number):
    answer = 0

    # 원소 세개씩 확인해야 하므로 배열 끝까지 확인 하지 않고 마지막 두개는 제외 시킨다.
    for i in range(0, len(number)-2):
        sum = 0
        # 첫번째 원소 다음부터 확인해줘야 해서 i+1
        for j in range(i+1,len(number)):
            # 두번째 원소 다응부터 확인해줘야 해서 j+1
            for z in range(j+1, len((number))):
                sum = number[i]+number[j]+number[z]
                if sum == 0:
                    answer += 1
    return answer


number = [0, 0, 1, -1, 0]
print(solution(number))