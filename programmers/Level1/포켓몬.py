def solution(nums):
    answer = 0

    # 고를 수 있는 포켓몬 수
    check = len(nums)//2
    print(check)

    # 제공해주는 포켓몬 종류를 담은 배열을 set을 통해 중복 제거
    nums = set(nums)
    print(nums)

    # 중복제거한 배열의 길이보다 고를 수 있는 포켓몬 수가 더 크다면, nums배열의 크기 그대로 출력
    if len(nums) < check:
        answer = len(nums)
    else:
    # 중복제거한 배열의 길이보다 고를 수 있는 포켓몬의 수가 더 작다면, 그대로 고를 수 있는 포켓몬 수 출력
        answer = check

    # ex1) nums=[1,2,3,4,5,5,5,5] 라면 전체 포켓몬의 종류의 수(len(nums))는 [1,2,3,4,5] =>총 5종류가 됩니다.
    # 하지만 최대 가져갈 수 있는 포켓몬은 최대 8마리중 절반인 4마리(check) 이므로 정답인 4를 return해야합니다. (nums>check)
    # ex2) nums=[1,2,3,4,5,5,5,5,5,5,5,5] 라면 최대 가져갈 수 있는 포켓몬의 마리수는 6마리(check)이지만
    # 전체 포켓몬의 종류의 수(nums)는 ex1과 마찬가지로 5이므로 5를 return해야합니다. (nums < check)

    return answer

nums = [3,1,2,3]
print(solution(nums))