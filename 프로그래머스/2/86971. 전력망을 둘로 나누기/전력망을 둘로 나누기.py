from collections import deque

def solution(n, wires):
    g = [[] for _ in range(n+1)]
    for i in wires:
        g[i[0]].append(i[1])
        g[i[1]].append(i[0])
        
    mn = n
    for i in wires:
        t1 = c(n, g, i[0], i[1])
        t2 = c(n, g, i[1], i[0])
        t = abs(t1-t2)
        if t<mn:
            mn = t
            
    return mn

def c(n, g, i1, i2):
    vis = [False]*(n+1)
    vis[i1]=True
    q = deque([])
    q.appendleft(i2)
    vis[i2]=True
    count = 1
    while(q):
        tmp = q.pop()
        for i in g[tmp]:
            if vis[i]==False:
                count+=1
                q.appendleft(i)
                vis[i]=True
            
    return count
    
    
    