arr = list(map(int, input().split()))

check = [1, 1, 2, 2, 2, 8]
type(check)
for i in range(len(check)):
    print(f"{check[i]-arr[i]} ", end="")