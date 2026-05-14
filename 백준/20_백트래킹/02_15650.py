n, m = map(int, input().split())
arr = []
def f(start):
    if len(arr)==m:
        print(*arr)
        return
    for i in range(start, n+1):
        arr.append(i)
        f(1)
        arr.pop()

f(1)