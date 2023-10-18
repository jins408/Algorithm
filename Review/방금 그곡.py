def replacement(data):
    data = data.replace('C#','c')
    data = data.replace('D#','d')
    data = data.replace('G#','g')
    data = data.replace('A#','a')
    data = data.replace('F#','f')

    return data

def solution(m, musicinfos):
    answer = ''
    m = replacement(m)

    max_time = 0
    for music in musicinfos:
        start, end, title, info = music.split(',')

        play_music = (int(end[:2])-int(start[:2]))*60+(int(end[3:])-int(start[3:]))

        value = ''
        index = 0
        time = play_music
        while time:
            value += info[index]
            if index+1 == len(info):
                index = -1
            index += 1
            time -= 1

        if m in value:
            if answer:
                if max_time >= play_music:
                    continue
            max_time = play_music
            answer = title

    if answer == '':
        return '(None)'
    else:
        return answer

    return answer

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))