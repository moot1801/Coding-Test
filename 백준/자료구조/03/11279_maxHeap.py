import heapq as h
import sys
input = sys.stdin.readline
hq = []

N = int(input())
for i in range(N):
    cmd = int(input())
    if cmd == 0:
        print(h.heappop(hq)*-1 if len(hq)!=0 else 0)
    else:
        h.heappush(hq, cmd*-1)
