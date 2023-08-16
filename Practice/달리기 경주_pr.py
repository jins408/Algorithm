def solution(players, callings):
    answer = []
    #["mumu", "soe", "poe", "kai", "mine"]
    playe = {}
    for i in range(len(players)):
        playe[players[i]]=i
    print(playe)
    for call in callings:
        #현재순위
        current_rank = playe[call]
        print(current_rank)
        # 바뀔 순위
        playe[call] -= 1
        playe[players[current_rank-1]] += 1

        # 순위를 서로 바꿔줘야함 3->2 2->3(players 리스트에서)
        players[current_rank] = players[current_rank-1]
        players[current_rank-1] = call

    return players

players= ["mumu", "soe", "poe", "kai", "mine"]
callings= ["kai", "kai", "mine", "mine"]
print(solution(players,callings))