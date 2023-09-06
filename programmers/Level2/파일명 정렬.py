#first:변수 3개를 만듭니다 head number tail
#second: for문을 돌리고 만약 해당 문자가 int형으로 했을때 false 나오면 head에넣고 true면 number에 넣습니다
#third: number의 길이가 0이 아니고 길이가 5가 되었을때는 나머지 부분을 tail에 넣으면 됩니다 이유)tail에도 숫자가 등장하기 때문입니다

def solution(files):
    answer = []

    head,number,tail = '', '', ''

    for file in files:
        for i in range(len(file)):
            if file[i].isnumeric():
                head = file[:i]
                number = file[i:i+6]

                for j in range(len(number)):
                    if not number[j].isnumeric():
                        tail = number[j:]
                        number = number[:j]
                        break
                answer.append([head, number, tail])
                head, number, tail = '', '', ''
                break

    answer.sort(key=lambda x:(x[0].upper(), int(x[1])))

    return [ ''.join(i) for i in answer]

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))