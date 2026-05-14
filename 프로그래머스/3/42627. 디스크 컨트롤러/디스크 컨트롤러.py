import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    l = len(jobs)
    heap = []
    hard = []
    fin = []
    time = 0
    task = 0
    while(len(fin) != l):
        # is fin?
        if hard!=[]:
            if hard[0][0] == hard[0][3]:
                fin.append(time-hard.pop()[1])
        # save : (작업시간, 요청시간, 작업번호, 시간)
        while task < l and jobs[task][0] <= time:
            heapq.heappush(heap, [jobs[task][1], jobs[task][0], task, 0])
            task+=1
        # take
        if len(heap)!=0 and hard==[]:
            hard.append(heapq.heappop(heap))
        # run 
        if len(hard)!=0:
            hard[0][3] += 1   
        time += 1
    answer = sum(fin)//len(fin)
    return answer