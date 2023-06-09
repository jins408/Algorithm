def check(place):
    # P='사람' O='빈책상' X='파티션'
    # 전달 받은 place는 1차원 배열로 이루어진 문자열을 2차원 배열로 만들어서 인덱스로 거리를 확인하기 위해 enumerate함수를 사용
    print(place)
    for idx_row, row in enumerate(place):
        for idx_col, cell in enumerate(row):
            print(idx_row, idx_col, cell)


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

#for pleac in places:
#    print(pleac)

def soultion(places):
    return [check(place) for place in places]

#print(soultion(places))

matrix = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(i,j,matrix[i][j])

