import sys
from collections import deque 
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
g = [[] for _ in range(N*M+1)]
v = [False for _ in range(N*M+1)]
c = [0 for _ in range(N*M+1)]

dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]
for i in range(N):
    tmp = list(map(int, input().strip()))
    arr.append(tmp)

for i in range(0, N*M):
    xi = i//M
    yi = i%M
    if arr[xi][yi]==0:
        v[xi*M+yi]=True
    else:
        for k in range(4):
            x = xi+dx[k]
            y = yi+dy[k]
            if (x >= 0 and 
                x < N and 
                y >= 0 and 
                y < M and
                arr[x][y]==1):
                g[i].append(x*M+y)

# BFS
# print(g, v)
q = deque()
q.append(0)
v[0]=True
c[0]=1
while q:
    target = q.popleft()
    for i in g[target]:
        if v[i]==False:
            if i==N*M:
                print("!", c[N*M]+1)
                exit(1)
            q.append(i)
            v[i]=True
            c[i]=c[target] + 1

print(c[N*M-1])


