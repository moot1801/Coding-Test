def solution(genres, plays):
    answer = []
    arr = [(idx, x, genres[idx]) for idx, x in enumerate(plays)]
    arr.sort(key = lambda x: (-x[1], x[0]))
    
    types = set([x[2] for x in arr])
    book = {}
    for i in arr:
        if i[2] not in book:
            book[i[2]] = []
        book[i[2]].append((i[0], i[1]))
    
    book = dict(sorted(book.items(), key = lambda x: -sum([y[1] for y in x[1]])))
    print(book)
    for i in book:
        target = book[i]
        if len(target) > 2:
            answer.extend([x[0] for x in target[:2]])
        else:
            answer.extend([x[0] for x in target])
    return answer