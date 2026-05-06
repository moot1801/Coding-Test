def solution(phone_book):
    answer = True
    phone_book.sort()
    n = len(phone_book)
    for i in range(n-1):
        target = phone_book[i]
        l = len(target)
        if target == phone_book[i+1][:l]:
            return False
    return True