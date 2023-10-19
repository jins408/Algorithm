def solution(book_time):
    answer = 0
    book_time_int = []

    for a, b in book_time:
        book_time_int.append([int(a[:2])*60+int(a[3:]),1])
        book_time_int.append([int(b[:2])*60+int(b[3:]),0])

    print(book_time_int)
    book_time_int.sort()

    now = 0
    for time in book_time_int:
        if time[1] == 1:
            now +=1
        else:
            now -=1

        answer = max(answer, now)


    return answer

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
print(solution(book_time))
