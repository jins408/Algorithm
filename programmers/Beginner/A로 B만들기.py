def solution(before, after):
    answer = 0

    a = sorted(before)
    b = sorted(after)

    temp = []
    for i in range(len(a)):
        if a[i] == b[i]:
            temp.append(a[i])
        else:
            temp.append(1)

    if 1 in temp:
        return 0
    else:
        return 1

before = "allpe"
after = "apple"
#"olleh"
#"hello"
print(solution(before, after))