import heapq
def solution(operations):
    min_heap = []
    max_heap = []
    visited = [False]*1000000
    idx = 0
    for i in operations:
        oper, num = i.split(" ")
        num = int(num)
        if oper=="I": # 큐에 삽입
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            idx += 1
        else:
            if num==1: # 최대 삭제
                while(max_heap):
                    tmp = heapq.heappop(max_heap)[1]
                    if visited[tmp]==False:
                        visited[tmp]=True
                        break
            else: # 최소 삭제
                while(min_heap):
                    tmp = heapq.heappop(min_heap)[1]
                    if visited[tmp]==False:
                        visited[tmp]=True
                        break
    mx, mn = 0, 0
    if all(visited[:idx])==False:
        while(max_heap):
            tmp = heapq.heappop(max_heap)
            if visited[tmp[1]]==False:
                break
        mx = -tmp[0]
        while(min_heap):
            tmp = heapq.heappop(min_heap)
            if visited[tmp[1]]==False:
                break
        mn = tmp[0]
    return [mx, mn]