import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sets = [i for i in range(n+1)]
sizes = [1 for i in range(n+1)]
def find(x):
    if sets[x]!=x:
        sets[x] = find(sets[x])
    return sets[x]

def union(a, b):
    ra = find(a)
    rb = find(b)
    if sizes[ra] < sizes[rb]:
        ra, rb = rb, ra
    sets[rb] = ra
    sizes[ra] += sizes[rb]

for j in range(m):
    action, a, b = map(int, input().split())
    if action:
        print("YES" if find(a)==find(b) else "NO")
    else:
        union(a, b)