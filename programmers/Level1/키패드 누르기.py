def solution(numbers, hand):
    answer = ''

    keypad = {'1':(0,0), '2':(0,1), '3':(0,2),
              '4':(1,0), '5':(1,1), '6':(1,2),
              '7':(2,0), '8':(2,1), '9':(2,2),
              '*':(3,0), '0':(3,1), '#':(3,2)}

    left = keypad['*']  #왼손
    right = keypad['#'] #오른손

    for number in numbers:
        # 거리를 구하기위해 현재 위치를 알아야 함
        now = keypad[str(number)]
        if number == 1 or number == 4 or number == 7:
            answer += "L"
            left = keypad[str(number)]
        elif number == 3 or number == 6 or number == 9:
            answer += "R"
            right = keypad[str(number)]
        else:
            # 거리구하기
            dic_r = 0
            dic_l = 0
            # zip를 이용해 거리를 구해주기
            # 이동거리를 카운트 해줘야 하기때문에 계산한값을 abs(절대값)으로 처리해줌
            for a,b,c in zip(right,left,now):
                dic_r += abs(a-c)
                dic_l += abs(b-c)
            # 오른쪽이 이동수가 적은경우 오른손
            if dic_r < dic_l:
                answer += "R"
                right = now
            # 왼쪽이 이동수가 적은경우 왼손
            elif dic_r > dic_l:
                answer += "L"
                left = now
            # 오른쪽, 왼쪽 이동수가 동일한 경우
            else:
                # 오른손잡이면 오른쪽
                if hand == "right":
                    answer += "R"
                    right = now
                # 아니면 왼손
                else:
                    answer += "L"
                    left = now

    return answer

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    #[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    #[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "left"
    #"left"
    #"right"
print(solution(numbers, hand))
