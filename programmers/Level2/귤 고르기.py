def solution(k, tangerine):
    answer = 0

    dic = {}
    for i in tangerine:
        d = dic.get(i)
        # 참조하고자 하는 키가 존재하지 않더라도 에러를 발생시키지 않고 None값을 리턴해준다
        if d == None:
            # 빈 딕셔너리에 당연히 key값들은 존재하지 않기 때문에 dic[i]=1로 값을 넣어줌
            dic[i] = 1
        else:
            dic[i] += 1

    # 내림차순으로 정렬
    num = sorted(dic.values(), reverse=True)
    sum = 0
    cnt = 0
    for i in num:
        sum += i
        cnt += 1
        # sum이 k보다 크거나 같으면 cnt값을 리턴
        if k <= sum:
            answer = cnt
            break

    return answer

k = 2
tangerine =[1, 1, 1, 1, 2, 2, 2, 3]
    #[1, 1, 1, 1, 2, 2, 2, 3]
    #[1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))