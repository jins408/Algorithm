from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    # 모든경우의 수를 찾는다.(조합)
    # 한 배열에 대한 조합을 해주는 combinations 모듈
    # 각 원소의 중복 갯수를 세주는 counter 모듈
    for c in course:
        temp = []
        for order in orders:
            # course의 원소의 숫자 만큼 조합을 만들어준다. 숫자2면 2개로만 조합을 만들어줌
            # orders의 문자열을 하나씩 다 돌면서 알파벳 2개만 가지고 조합을 만들어준자. ex) "ABCFG"->"AB"
            combi = combinations(sorted(order), c)
            temp += combi

        # Counter모듈을 사용해 조합의 중복 갯수를 세준다.
        # 딕셔너리 형태로 만들어짐 ex){(A,B) : 2 ,(A,C) : 1, (A,D) : 1 ,(B,C) : 1 ,(B,D) : 1, (C,D) : 1}
        counter = Counter(temp)

        # 길이가 0아 아니고 counter != 1이 아니면 (최소 주문건이 2명 이상이것만 조합으로 만들수 있기때문에 조건을 걸어줌)
        if len(counter) != 0 and max(counter.values()) != 1:
            for f in counter:
                # 가장 많이 겹치는 조합을 새로운 메뉴구성으로 만드는 것이기 때문에 max(counter.value())값과 같은 value값을 가진 key를 찾아서 넣어준다.
                if counter[f] == max(counter.values()):
                    answer += [''.join(f)]

    # 알파벳도 오름차순으로 정렬해야 하기때문에 sorted를 해준다.
    return sorted(answer)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))