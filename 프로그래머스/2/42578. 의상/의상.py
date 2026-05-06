def solution(clothes):
    answer = 1
    dic = {}
    for item, itype in clothes:
        if itype not in dic:
            dic[itype] = []
        dic[itype].append(item)
    for i in dic:
        answer *= len(dic[i])+1
            
    return answer - 1