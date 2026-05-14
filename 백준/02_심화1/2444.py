n = int(input())
# 0 : 4 1
# 1 : 3 3
# 2 : 2 5
# 3 : 1 7
# 4 : 0 9
# 5 : 1 7
# 6 : 2 5
for i in range(2*n-1):
    for j in range(abs(n-1-i)):
        print(" ", end="")
    if i//n>0:
        for j in range(2*n-1+2*(-i+n-1)):
            print("*", end="")
    else:
        for j in range(2*i+1):    
            print("*", end="")
    print()

