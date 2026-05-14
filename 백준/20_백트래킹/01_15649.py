n, m = map(int, input().split())

def track(arr, check, lv, tmp):
    if lv==m:
        print(*tmp)
        return 
    for i in range(len(check)):
        if check[i]==0:
            check[i]=1
            tmp.append(arr[i])
            track(arr, check, lv+1, tmp)
            tmp.pop()
            check[i]=0

arr = range(1, n+1)
check = [0 for i in range(n)]
lv = 0
value = []
for i in range(n):
    tmp = []
    tmp.append(arr[i])
    check[i]=1
    track(arr, check, lv+1, tmp)
    check[i]=0