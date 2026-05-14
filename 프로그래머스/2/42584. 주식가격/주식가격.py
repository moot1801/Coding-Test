from collections import deque
def solution(prices):
    answer = [0 for x in range(len(prices))]
    arr = deque(prices)
    l = 0
    while(len(arr)>0):
        tmp = arr.popleft()
        for i in arr:
            answer[l]+=1
            if i < tmp:
                break
        l += 1
    return answer