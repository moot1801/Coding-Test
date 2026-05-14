# [2026-01-01~2026-01-04]
arr = [list(map(int, input().split())) for _ in range(9)]
empty_list = []
for i in range(9):
    for j in range(9):
        if arr[i][j]==0:
            empty_list.append((i,j))

def backtrack(idx):
    if idx==len(empty_list):
        for row in arr:
            print(*row)
        exit(0)
    x, y = empty_list[idx]
    values = check(x, y)
    for value, flag in enumerate(values[1:], start=1):
        if flag==0:
            arr[x][y] = value
            backtrack(idx+1)
            arr[x][y] = 0

def check(x, y):
    solution = [0 for i in range(10)]
    for i in arr[x]:
        solution[i]+=1
    for i in range(9):
        solution[arr[i][y]] += 1
    nx, ny = (x//3)*3, (y//3)*3
    for i in range(3):
        for j in range(3):
            solution[arr[nx+i][ny+j]] += 1
    return solution

backtrack(0)
