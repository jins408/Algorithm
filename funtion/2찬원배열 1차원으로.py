list1 = [[1, 10], [2, 22], [3, 19], [4, 7]]
list2 = [data for inner_list in list1 for data in inner_list]
#print(list2)

list2 = []
for inner_list in list1:
    for data in inner_list:
        list2.append(data)
print(list2)


# 1차원 문자열 각각 원소별로 나눠서 2차원 리스트로 만들기

m = 4
n = 5
board =["CCBDE", "AAADE", "AAABF", "CCBBF"]
board = [list(board[i]) for i in range(m)]
print(board)


