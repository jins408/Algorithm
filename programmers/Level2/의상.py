def solution(clothes):
    answer = 0

    # 부위별로 몇개인지 개수를 담을 딕녀너리 (얼굴,상의,하의,겉옷)
    dic = {}
    for clothe in clothes:
        d = dic.get(clothe[1])
        if d == None:
            dic[clothe[1]] = 1
        else:
            dic[clothe[1]] +=1

    # 각 부위별 옷의 개수를 +1해서 곱해줌
    sum = 1
    for value in dic.values():
        sum *= value+1

    # 마지막으로 -1
    answer = sum-1

    return answer

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    #[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))