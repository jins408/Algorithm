def solution(phone_book):
    answer = True

    # 문자열 리스트를 정렬해주면,
    # ["119", "1195524421", "97674223"]
    #  문자열 안의 숫자가 작은 값부터 정렬된다. -> 맨앞의 문자와 바로 다음 문자를 비교했을떼, 같아면 접두어이기때문에 바로 return해준다.
    phone_book.sort()
    for i in range(len(phone_book)-1):
        a = phone_book[i]
        # 첫번째 문자 "119"와 다음 문자를 비교할때 접두어를 찾는거기 때문에 첫문자의 길이와 같은 부분까지만 비교해서
        # 일치하면 False (접두어를 포함한 것이기 때문에)
        if a == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            return answer

    return answer

phone_book = ["119", "97674223", "1195524421"]
    #["12","123","1235","567","88"]
    #["119", "97674223", "1195524421"]
print(solution(phone_book))