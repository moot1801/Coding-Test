# 11:37
# 문제

#  $N$ 명의 사람들이 한 줄로 서 있다. 각 사람은 왼쪽에서 오른쪽으로 순서대로 $1, 2, \ldots, N$ 의 번호가 붙어 있다. $i$ 번 사람의 키는 $A_i$ 이다. $i$ 번 사람과 $j$ 번 사람의 거리는 $|i - j|$ 이다.

# 모든 $i$ 에 대해서, 키가 $A_i - K$ 이상 $A_i$ 이하면서, 나의 오른쪽에 서 있지 않은 사람들 중 가장 먼 사람을 찾고, 그 사람과의 거리를 합한 것을 출력하라. $i$ 번 사람에 대해 자신은 위 조건을 만족하기 때문에, 항상 그러한 사람들은 존재한다.
# 입력

# 파일의 첫째 줄에 테스트 케이스의 개수를 나타내는 자연수 $T$ 가 주어지고,

# 이후 차례로 $T$ 개의 테스트 케이스가 주어진다. ($1 \le T \le 31$)

# 각 테스트 케이스의 첫 줄에는 정수 $N, K$ 가 주어진다. ($1 \le N \le 200\,000, 0 \le K \le 500\,000$)

# 다음 줄에는 $N$ 개의 정수 $A_1, \ldots, A_N$ 이 주어진다. ($0 \le A_i \le 500\,000$)

# 모든 테스트 케이스들에 대한 $N$ 의 합은 $2\,000\,000$ 이하이다.
# 출력

# 각 테스트 케이스마다 첫 줄에는 Case #$C$ 를 출력하여야 한다. 이때 $C$는 테스트 케이스의 번호이다.

# 다음 줄에는 문제의 정답을 출력한다.
NUMBER = 500001
test_case = int(input())
for i in range(1, test_case+1):
    result=0
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    targets=[NUMBER for _ in range(500001)]
    for idx, j in enumerate(arr):
        if targets[j]==NUMBER:
            targets[j]=idx
        con = j-K if j-K>=0 else 0
        m = min(targets[con:j+1])
        if m==NUMBER:
            continue
        result += abs(m-idx)
        

    print(f"Case #{i}")
    print(result)
