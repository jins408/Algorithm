def solution(phone_book):
    answer = True

    phone_book.sort()
    for i in range(len(phone_book)-1):
        a = phone_book[i]
        if a == phone_book[i+1][:len(a)]:
            answer = False
            return  answer
    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))