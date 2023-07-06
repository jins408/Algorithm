# arr1, arr2 배열의 원소들을 2진법으로 바꾸고 map1배열에 담아서 return 해줌
def map(n, arr):
    map1 = [[0] * n for _ in range(n)]
    i = 0
    while arr[i] >= 0:
        num = arr[i]
        for i in range(i, i + 1):
            for j in range(len(map1) - 1, -1, -1):
                b = num % 2
                num //= 2
                map1[i][j] = b
            if num < 1:
                break
        i += 1
        if i >= n:
            break
    return map1

def solution(n, arr1, arr2):
    answer = []
    get_map1 = map(n, arr1)
    get_map2 = map(n, arr2)

    # 2진법으로 바꾼 get_map1와 get_map2를 1,0을 비교하여 합쳐줌
    pwd = [[0] * n for _ in range(n)]
    for i in range(len(get_map1)):
        for j in range(len(get_map2)):
            if get_map1[i][j] == 1 or get_map2[i][j] == 1:
                pwd[i][j] = 1
            else:
                pwd[i][j] = 0

    # 합친 pwd배열을 보고 둘중에 하나라도 1이면 ->#으로 둘다 0이면 ->공백으로 처리해서 빈문자열인 a에 넣어줌
    a = ''
    for i in range(len(pwd)):
        for j in range(len(pwd)):
            if pwd[i][j] == 1:
                a+='#'
            else:
                a+=' '
        a += ','
    # 마지막 , 값을 제거하고
    a = a[:-1]
    # ,기준으로 잘라서 answer에 넣어줌
    answer = a.split(',')

    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n,arr1, arr2))