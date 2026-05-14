import heapq
import sys
input=sys.stdin.readline

N = int(input())
hq = []
for i in range(N):
    cmd = int(input())
    if cmd==0:
        print(heapq.heappop(hq)[1] if len(hq)!=0 else 0)
    else:
        heapq.heappush(hq, (abs(cmd), cmd))