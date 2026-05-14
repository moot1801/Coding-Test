s = input()
solution = set()
l = len(s)

for i in range(len(s)):
    for j in range(len(s)):
        if i+j<l:
            solution.add(s[j:i+j+1])

print(len(solution))

