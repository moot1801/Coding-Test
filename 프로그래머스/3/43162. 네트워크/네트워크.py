from collections import deque

def solution(n, computers):
    answer = 0
    vis = [False for _ in range(n+1)]
    g = [[] for _ in range(len(computers)+1)]
    q = deque([])
    for i in range(len(computers)):
        for j in range(len(computers)):
            if computers[i][j]==1 and i!=j:
                g[i].append(j)
    for current in range(n):
        if not vis[current]:
            vis[current]=True
            answer+=1
            q.append(current)
            while(q):
                cnt = q.popleft()
                for i in g[cnt]:
                    if not vis[i]:
                        q.append(i)
                        vis[i]=True
        
    return answer