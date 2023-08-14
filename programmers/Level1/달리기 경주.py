def solution(players, callings):
    answer = []

    # {플레이어:등수} 딕셔너리를 만들기 위해
    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i
    print(dic)
    # {'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4}

    # 등수와 플레이러를 비교해서 players(list)에 있는 값들을 서로 바꿔줌
    for call in callings:
        # 현재등수
        current_rank = dic[call] # dic[call] = 3 call='kai'

        # {플레이어:등수} 등수 바꿔주기 위한 인덱스 값 찾기 // -1, +1
        dic[call] -= 1  # 3-1=2 (kai = 2 , poe = 3)으로 바껴야 하기 때문에
        dic[players[current_rank-1]] += 1 # players[3-1]->"poe" dic["poe"] = 2 -> 2+1 = 3

        # player리스트에서 서로 바뀐값 찾아서 값 바꿔주기
        #players[current_rank-1] ,players[current_rank] = call, players[current_rank-1]
        players[current_rank] = players[current_rank-1]
        # players[3] = "poe"
        players[current_rank-1] = call
        # players[2] = "kai"

    return players


players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))