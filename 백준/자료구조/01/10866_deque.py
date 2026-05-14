
# 문제

# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여덟 가지이다.

#     push_front X: 정수 X를 덱의 앞에 넣는다.
#     push_back X: 정수 X를 덱의 뒤에 넣는다.
#     pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#     pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#     size: 덱에 들어있는 정수의 개수를 출력한다.
#     empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
#     front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#     back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 입력

# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

class Deque:
    def __init__(self, size):
        self.s=size
        self.values=0
        self.d=[0]*self.s
        self.pnt=1 # front
        self.pre=0 # back
    def push_front(self, x):
        self.d[self.pnt]=x
        self.pnt = (self.s+self.pnt+1)%self.s
        self.values+=1
    def push_back(self, x):
        self.d[self.pre]=x
        self.pre = (self.s+self.pre-1)%self.s
        self.values+=1
    def pop_front(self):
        if self.empty():
            return -1
        result=self.d[(self.pnt-1)%self.s]
        self.pnt = (self.s+self.pnt-1)%self.s
        self.values-=1
        return result
    def pop_back(self):
        if self.empty():
            return -1
        result=self.d[(self.pre+1)%self.s]
        self.pre = (self.s+self.pre+1)%self.s
        self.values-=1
        return result
    def size(self):
        return self.values
    def empty(self):
        if self.values==0:
            return 1
        else:
            return 0
    def front(self):
        if self.empty():
            return -1
        return self.d[(self.pnt-1)%self.s]
    def back(self):
        if self.empty():
            return -1
        return self.d[(self.pre+1)%self.s]
    
import sys
input = sys.stdin.readline

n = int(input())
s=Deque(10001)
for i in range(n):
    cmd = input().split()
    if cmd[0] == "push_back":
        s.push_back(cmd[1])
    elif cmd[0] == "push_front":
        s.push_front(cmd[1])
    elif cmd[0] == "pop_front":
        print(s.pop_front())
    elif cmd[0] == "pop_back":
        print(s.pop_back())
    elif cmd[0] == "pop":
        print(s.pop())
    elif cmd[0] == "size":
        print(s.size())
    elif cmd[0] == "empty":
        print(s.empty())
    elif cmd[0] == "front":
        print(s.front())
    else:
        print(s.back())