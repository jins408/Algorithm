def solution(files):
    answer = []

    head, number, tail = '', '', ''

    for file in files:
        for i in range(len(file)):
            if file[i].isnumeric():
                head = file[:i]
                number = file[i:]

                for j in range(len(number)):
                    if not number[j].isnumeric():
                        tail = number[j:]
                        number = number[:j]
                        break
                answer.append([head, number, tail])
                head, number, tail  = '','',''
                break

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return [''.join(i) for i in answer]

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))
