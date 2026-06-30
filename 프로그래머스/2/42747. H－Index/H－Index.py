def solution(citations):
    arr = sorted(citations, reverse=True)
    h_index = 0
    for idx, i in enumerate(arr):
        if i >= idx+1:
            h_index = idx+1
        else:
            break
    return h_index
        
                    