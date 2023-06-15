def solution(price):
    answer = 0
    sale = [100000, 300000, 500000]

    if price < 100000:
        return price

    if sale[0] <= price < sale[1]:
        answer = price - (price*(5/100))
    elif sale[1] <= price < sale[2]:
        answer = price - (price*(10/100))
    elif sale[2] <= price :
        answer = price - (price*(20/100))

    return int(answer)


price = 100030
print(solution(price))