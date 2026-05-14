import sys
from collections import deque 
input=sys.stdin.readline

class Node:
    def __init__(self):
        self.chNode=[]
        self.state=0
    def link(self, x):
        self.chNode.append(x)

N = int(input())

graph = [Node() for _ in range(N+1)]

M = int(input())
for i in range(M):
    node_1, node_2 = map(int, input().split())
    graph[node_1].link(graph[node_2])
    graph[node_2].link(graph[node_1])

result = 0
q = deque()
q.append(graph[1])
while(len(q)>0):
    target = q.popleft()
    if target.state==0:
        target.state=1
        result+=1
    else:
        continue
    for i in target.chNode:
        if i.state==0:
            q.append(i)
    
print(result-1)