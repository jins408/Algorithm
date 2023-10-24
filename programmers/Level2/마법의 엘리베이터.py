def solution(storey):
    answer = 0

    while True:
        storey, moves = divmod(storey, 10)
        #print(storey, moves)
        if moves > 5 or ( moves == 5 and storey%10 >= 5):
            moves = 10-moves
            storey += 1
        answer += moves
        if storey == 0:
            break

    return answer

storey = 2554
print(solution(storey))