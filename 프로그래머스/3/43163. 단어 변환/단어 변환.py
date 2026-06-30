from collections import deque
def solution(begin, target, words):
    answer = 0
    words.append(begin)
    if target not in words:
        return 0
    g = makeGraph(words)
    l = len(words)
    q = deque()
    q.append([l-1, 0])
    vis = [False for _ in range(l+1)]
    vis[l] = True
    while(q):
        t, c = q.popleft()
        if words[t]==target:
            return c
        for i in g[t]:
            q.append((i, c+1))
            vis[i] = True
        
    
    return answer
def diff(word1, word2):
    solution=0
    l = len(word1)
    for i in range(l):
        solution += 0 if (ord(word1[i])-ord(word2[i])==0) else 1
    return solution
def makeGraph(words):
    l = len(words)
    g = [[] for _ in range(l)]
    for i in range(l):
        for j in range(l):
            if i!=j and diff(words[i], words[j])==1:
                g[i].append(j)
                g[j].append(i)
    for i in range(l):
        g[i] = list(set(g[i]))
    return g
        