def my_factorial(n):
    if(n > 1):
        return n * my_factorial(n - 1)
    else:
        return 1


def solution(n, k):
    answer = []

    # answer에 담기는 맨 처음 수는 k//(n - 1)+1
    # 이게 정해 졌으면 그 뒤에 순서대로 줄 세우는 경우의 수가 (n - 1)!
    num_list = [i for i in range(1, n+1)]
    while (n != 0):
        s = my_factorial(n-1)
        # k에서 (n - 1)!을 나눴을 때의 몫이 첫번째 오는 자리
        idx = k//s
        # k에서 (n - 1)!을 나눴을 때의 나머지가 다시 k로 오는 자리
        k = k%s
        if k == 0:
            answer.append(num_list.pop(idx-1))
        else:
            answer.append(num_list.pop(idx))
        n -= 1
    return answer


n = 3
k = 5
print(solution(n,k))