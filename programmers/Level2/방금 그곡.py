def replacement(data):
    data = data.replace('C#','c')
    data = data.replace('D#','d')
    data = data.replace('F#','f')
    data = data.replace('A#','a')
    data = data.replace('G#','g')

    return data

def solution(m, musicinfos):
    answer = ''
    # c#,d#,f#,g#,a#을 한글자 취급해주기 위해 변환하는 함수
    m = replacement(m)

    max_time = 0
    for music in musicinfos:
        # 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보
        start_time,end_time, title, music_info = music.split(",")
        music_info = replacement(music_info)

        # 시작시간과 끝시간의 차이를 분단위로 계산하여 play_time에 할당한다.
        play_time = (int(end_time[:2])-int(start_time[:2]))*60 + (int(end_time[3:])-int(start_time[3:]))
        index = 0
        value = ''
        time = play_time
        # time이 0이 될때까지, while문 반복
        while time:
            # value 문자열에 music_info[index]이어 붙이고
            value += music_info[index]
            # index+1이 music_info길이와 같다면, 다시 처음 music_info부터 시작해야하므로 index를 -1로 갱신해준다.
            if index+1 == len(music_info):
                index = -1
            index += 1
            time -= 1
        # m이 value에 존재하고 answer에 값이 이미 존재하고 max_time이 play_time보다 크거나 같다면 continue
        # -> 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환, 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환
        if m in value:
            if answer:
                if max_time >= play_time:
                    continue
            # m이 value에 존재하고 answer에 값이 없다면 max_time을 play_time으로 갱신하고 answer에 title을 할당
            max_time = play_time
            answer = title

    # answer에 값이 존재한다면 answer을 반환하고, 그렇지 않다면 '(None)'을 반환
    if answer:
        return answer
    else:
        return '(None)'

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m,musicinfos))