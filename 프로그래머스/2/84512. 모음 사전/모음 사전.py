def solution(word):
    arr = ['A', 'E', 'I', 'O', 'U']
    cnt = 0
    
    def DFS(current, word):
        nonlocal cnt, arr
        if (len(current) > 5):
            return False
        if current:
            cnt+=1
        if current==word:
            return True
        for i in arr:
            current.append(i)
            if DFS(current, word):
                return True
            current.pop()
    
    
    DFS([], list(word))
        
    
    return cnt

