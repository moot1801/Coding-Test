

n = int(input())

arr = [[1 for i in range(n)] for j in range(n)]

def f(x, y, n):
    if n==1:
        return 
    n = int(n/3)
    for a in range(x+n, x+2*n):
        for b in range(y+n, y+2*n):
            arr[a][b]=0

    
    for i in [x, x+n, x+2*n]:
        for j in [y, y+n, y+2*n]:
                f(i, j, n)

    return arr
    
solution = f(0, 0, n)

for i in solution:
    for j in i:
        if j==1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
