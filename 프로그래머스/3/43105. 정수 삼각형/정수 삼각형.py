def solution(triangle):
    answer = 0
    dp = {0:triangle[0][0]}
    for i in triangle[1:]:
        tmp = {}
        for idx, value in enumerate(i):
            candi = []
            if idx-1 in dp:
                candi.append(dp[idx-1]+value)
            if idx in dp:
                candi.append(dp[idx]+value)
            tmp[idx] = max(candi)
            
        dp = tmp
            
    return max(dp.values())