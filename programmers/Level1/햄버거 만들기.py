def solution(ingredient):
    answer = 0

    burger = []
    for i in ingredient:
        burger.append(i)
        # burger쌓이는 길이가 4이상일때 [1,2,3,1]와 같으면 되니까 burger[-4:]로 확인
        if burger[-4:] == [1,2,3,1]:
            # 동일하다면 answer+1 해주고
            answer +=1
            # buger에 1,2,3,1를 제거해준다(새로운 숫자들을 쌓아서 다시 비교해줘야 하기때문에)
            for _ in range(4):
                burger.pop()

    return answer

ingredient = [1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1]
    #[1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1]
    #[2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))