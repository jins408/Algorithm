import re
def solution(new_id):
    answer = ''

    # 0 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    # 0 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    # 0 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    # 0 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    # 0 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    #6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    #7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

    # 대문자 모두 소문자로 치환(1단계)
    id = new_id.lower()
    print(id)
    # 2단계
    id_new = ''
    for i in id:
        if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
            id_new += i
    print(id_new)

    # 마침표(.) 두개 이상이면 하나의 마침표(.)로 치환 (3단계)
    '''
    n_id = id_new[0]
    for i in range(1, len(id_new)):
        if id_new[i - 1] != id_new[i]:
            n_id += id_new[i]
    print(n_id)

    '''
    n_id = re.sub('\.+','.',id_new)
    print(n_id)
    # 마침표(.)가 처음이나 끝에 위치한다면 제거 (4단계)
    if len(n_id) == 1:
        if n_id[0] == '.':
            n_id = n_id[1:]
            if n_id == "":
            # 빈문자열을 a문자로 바꿈(5단계)
                n_id = n_id.replace("", "a")
                print(n_id)
    if len(n_id) >= 2:
        # 마침표가 처음에 존재할때
        if n_id[0] == '.':
            n_id = n_id[1:]
        # 마침표가 마지막에 존재할때
        if n_id[-1] == '.':
            n_id = n_id[:-1]
        n_id = n_id.replace(" ","a")

    if len(n_id) >= 16:
        n_id = n_id[0:15]
    print(n_id)
    if n_id[-1] == '.':
        n_id = n_id[:-1]

    if len(n_id) <= 2:
        while True:
            n_id += n_id[-1]
            if len(n_id) >= 3:
                break
    answer = n_id
    return answer

new_id="...!@BaT#*..y.abcdefghijklm"
    #"=.="
    #"z-+.^."
    #"...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))

