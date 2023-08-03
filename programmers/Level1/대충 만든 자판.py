# 일치하는 문자 중에 작은 인덱스 값을 찾기 위한 함수
def fun(keymap, target):
    index = []
    for k, key in enumerate(keymap):
        for idx, i in enumerate(key):
            if target == i:
                # 1부터 시작하기때문에 idx+1해줌
                index.append(idx+1)
    # 일치하는 값이 없는 경우 0을 return
    if len(index) == 0:
        return 0
    else:
        # 인덱스 값이 찾은 값을 찾아서 return
        return min(index)

def solution(keymap, targets):
    answer = []

    for target in targets:
        cnt = 0
        for i in range(len(target)):
            get_fun = fun(keymap, target[i])
            cnt+=get_fun
            # get_fun=0이면 일치하는게 없다는 뜻
            # 목표 문자열을 작성할 수 없을 때 -1을 return 해줘야 함
            if get_fun == 0:
                cnt = -1
                break
        # 일치하는게 있다면, 다 더해줘서 answer에 cnt를 넣어줌
        if cnt != 0:
            answer.append(cnt)
    return answer

keymap =  ["AA", "BB", "CC"]
    #["BC", "CDB"] 2
    #["ABCE"] [-1]
    #["BC"] [-1, 3]
    #["AGZ", "BSSS"]
    #["ABACD", "BCEFD"]
targets = ["DF","RT","EE","AA","AC"]
    #["BB"]
    #["ABDE"]
    #["AC","BC"]
    #["ASA","BGZ"]
    #["ABCD","AABB"]
print(solution(keymap, targets))