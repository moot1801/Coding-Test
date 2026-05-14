import sys
from collections import deque 
import heapq
import copy
input=sys.stdin.readline

N, M, V = map(int, input().split())

g = [[] for _ in range(N+1)]
q = deque()
vd = [False] * (N+1)
vb = [False] * (N+1)
for i in range(M):
    n1, n2 = map(int, input().split())
    heapq.heappush(g[n1], n2)
    heapq.heappush(g[n2], n1)

g2 = copy.deepcopy(g)
#print(g)

# DFS
def DFS(target):
    if not vd[target]:
        print(target, end=" ")
        vd[target] = True
    for i in range(len(g[target])):
        k = heapq.heappop(g[target])
        if not vd[k]:
            print(k, end=" ")
            vd[k] = True
            DFS(k)
DFS(V)
print()
# BFS
q.append(V)
while(q):
    target = q.popleft()
    if not vb[target]:
        print(target, end=" ")
        vb[target]=True
        for i in range(len(g2[target])):
            k = heapq.heappop(g2[target])
            q.append(k)
