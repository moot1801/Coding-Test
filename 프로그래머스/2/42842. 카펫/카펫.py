

def solution(brown, yellow):
    candi = f(brown+yellow)
    for i in candi:
        if 2*i[0]+2*i[1]-4==brown:
            return i
    

def f(n):
    answer = []
    cand = [x for x in range(1, int((n+1)/2)+1)]
    while(cand):
        i = cand.pop()
        if n%i==0 and i>2 and n/i>2 and any([n/i in cand, n/i==i]):
            answer.append([i, int(n/i)])
    return answer