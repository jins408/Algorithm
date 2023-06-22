def solution(keyinput, board):
    answer = []

    x = 0
    y = 0

    max_x = board[0]//2
    min_x = -(board[0]//2)
    max_y = board[1]//2
    min_y = -(board[1]//2)

    for i in range(len(keyinput)):
        if keyinput[i] == "left":
            x -= 1
            if x < min_x:
                x = min_x
        elif keyinput[i] == "right":
            x += 1
            if x > max_x:
                x = max_x
        elif keyinput[i] == "up":
            y += 1
            if y > max_y:
                y = max_y
        else:
            y -= 1
            if y < min_y:
                y = min_y

    answer = [x, y]
    return answer

keyinput =  ["left", "left", "left", "left", "right", "right", "right", "right"]
board =  [5,5]

print(solution(keyinput, board))