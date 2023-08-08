def solution(numbers, hand):
    answer = ''

    keypad = {'1':(0,0), '2':(0,1), '3':(0,3),
              '4':(1,0), '5':(1,1), '6':(1,2),
              '7':(2,0), '8':(2,1), '9':(2,2),
              '*':(3,0), '0':(3,1), '#':(3,2)}

    left = keypad['*']  #왼손
    right = keypad['#'] #오른손

    for number in numbers:
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
            for a,b,c in zip(right,left,now):
                dic_r += abs(a-c)
                dic_l += abs(b-c)
            if dic_r < dic_l:
                answer += "R"
                right = now
            elif dic_r > dic_l:
                answer += "L"
                left = now
            else:
                if hand == "right":
                    answer += "R"
                    right = now
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
