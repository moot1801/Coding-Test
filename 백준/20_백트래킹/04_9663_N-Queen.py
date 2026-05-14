# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

import sys

n = int(sys.stdin.readline())
count = 0

v_col = [False] * n            
v_diag1 = [False] * (2 * n)   
v_diag2 = [False] * (2 * n)   

def dfs(row):
    global count
    
    if row == n:
        count += 1
        return

    for col in range(n):
        if not v_col[col] and not v_diag1[row + col] and not v_diag2[row - col + n - 1]:
            v_col[col] = True
            v_diag1[row + col] = True
            v_diag2[row - col + n - 1] = True
            dfs(row + 1)
            v_col[col] = False
            v_diag1[row + col] = False
            v_diag2[row - col + n - 1] = False

dfs(0)
print(count)