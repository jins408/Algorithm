def solution(book_time):
    answer = 0

    book_time_int = []

    # 입실시간, 퇴실시간 시간을 분으로 바꿔서 전체시간을 분으로 표시
    # 방 정리하는 시간 10분이 필요하므로, 퇴실 시간에 +10을 해준다.
    # 입실,퇴실 인지 구분 값 필요 (입실:1 퇴실:0)
    for start, end in book_time:
        book_time_int.append([int(start[:2])*60+int(start[3:]),1])
        book_time_int.append([int(end[:2])*60+int(end[3:])+10,0])

    # book_time_int 리스트 정렬
    book_time_int.sort()

    now = 0
    # 현재 사용중인 방 갯수에 현재시간에 +1 해준다.
    for time in book_time_int:
        if time[1] == 1:
            now += 1
        else:
            # 퇴실시간이면 현재시간에서 -1 해준다.
            now -= 1

        # 방 개수의 최댓값을 계속 갱신해 나간다.
        answer = max(answer, now)

    return answer

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
print(solution(book_time))