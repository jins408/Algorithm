def solution(files):
    answer = []

    head,number,tail = '', '', ''

    for file in files:
        for i in range(len(file)):
            # 처음으로 숫자가 나온 i인덱스에서 head와 number로 분리
            if file[i].isnumeric():
                head = file[:i] # 숫자 나오기 전까지만
                number = file[i:] # 숫자나온 후 부터 끝까지

                for j in range(len(number)):
                    if not number[j].isnumeric():
                        # number로 tail 구분
                        tail = number[j:]   # 숫자 안나오면 TAIL
                        number = number[:j] # 첫부터 숫자가 나온 부분까지만
                        break
                # answer 리스트에 담아주고
                answer.append([head, number, tail])
                # 다시 변수들 초기화
                head, number, tail = '', '', ''
                break

    # 첫번째 인자 기준으로 오름차순으로 정렬하고 x[0]-> 첫번재 인자 head를 대,소문자 구분하지 않는다고 했기 때문에 upper(),lower()중 아무거나 해줌
    # 그리고 그 안에 다음 두번째 인자를 기준으로 오른차순 정렬 x[1] -> 두번째 인자 사전순으로 정렬해야 하기 때문에 문자열형태를 숫자(int)형으로 바꿔준다.
    # 내림차순으로 하고싶은 경우에는 -x[1] 앞에 -(마이너스)를 붙이면 됌
    answer.sort(key=lambda x:(x[0].upper(), int(x[1])))

    # 원래 형태로 만들어 주기 위해 .join 사용
    return [ ''.join(i) for i in answer]

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))