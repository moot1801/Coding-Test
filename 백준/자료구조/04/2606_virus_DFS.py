import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.chNode=[]
        self.state=0
    def link(self,x):
        self.chNode.append(x)

def DFS(start_node):
    if start_node.state!=0:
        return 0
    else:
        start_node.state=1
        for i in start_node.chNode:
            DFS(i)
        return 1

N = int(input())

graph = [Node() for _ in range(N+1)]

M = int(input())
for i in range(M):
    start, end = map(int, input().split())
    graph[start].link(graph[end])

result=0
DFS(graph[1])
for k in range(2, N+1):
    if graph[k].state==1:
        result+=1
print(result)