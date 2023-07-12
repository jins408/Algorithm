def solution(cards1, cards2, goal):
    answer = ''

    cad1 = ''
    cad2 = ''
    # goal 만들고자 하는 문장을 cards1와 cards2비교에서 문자열을 잘라줌
    for i in goal:
        if i in cards2:
            cad2 += i+' '
        else:
            cad1 += i+' '

    cad1 = cad1[:-1]
    cad2 = cad2[:-1]

    cad1 = cad1.split(' ')
    print(cad1)
    cad2 = cad2.split(' ')
    print(cad2)

    # goal에는 없지만 card에는 존재는 문자가 있을 수 있으므로 cad1_temp,cad2_temp에 존재하는 문자열에 넣어줌
    cad1_temp = ''
    for i in cards1:
        if i not in goal:
            cad1_temp += i+' '
    cad2_temp = ''
    for j in cards2:
        if j not in goal:
            cad2_temp += j+' '

    # 문자열이 존재하지 않는 경우는 공백으로 처리(나중에 cad1과 cad1_temp더해 줄때 오류가 발생할 수 있으므로)
    if cad1_temp == '':
        cad1_temp = ''
    else:
        cad1_temp = cad1_temp[:-1]
        cad1_temp = cad1_temp.split(' ')
    if cad2_temp =='':
        cad2_temp = ''
    else:
        cad2_temp = cad2_temp[:-1]
        cad2_temp = cad2_temp.split(' ')

    # 공백은 더해주지 않기 위해서 길이가 1이상인 것만 더해줌
    if len(cad1_temp) > 0:
        a = cad1 + cad1_temp
    else:
        a = cad1

    if len(cad2_temp) > 0:
        b = cad2 + cad2_temp
    else:
        b = cad2

    # goal문장과 순서가 동일하고, cards에 존재하는 문자열로 확인 한 후, 결과를 return
    if a == cards1 and b == cards2:
        return "Yes"
    else:
        return "No"

cards1 =  ["i", "drink", "water"]
cards2 =  ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
#  ["i", "drink", "water"], ["want", "to", "juice"], ["i", "want", "to", "drink", "water"]
print(solution(cards1, cards2, goal))