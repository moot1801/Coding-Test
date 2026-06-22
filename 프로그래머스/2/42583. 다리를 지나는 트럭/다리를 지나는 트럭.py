from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    wait = deque(truck_weights)
    ing = deque([])
    fin = deque([])
    time=0
    w = 0
    while(len(ing)+len(wait)>0):
        #print(time,"/", *fin,"/", *ing,"/", *wait)
        time += 1 
        # ing->fin?
        if ing and time-ing[0][1]>bridge_length-1:
            v, t = ing.popleft()
            fin.append(v)
            w -= v
        # wait->ing
        if wait and wait[0]+w<=weight:
            tmp = wait.popleft()
            ing.append((tmp, time))
            w += tmp
        
    
    return time