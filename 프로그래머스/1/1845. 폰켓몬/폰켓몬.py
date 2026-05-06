from collections import Counter
def solution(nums):
    answer = 0
    n = len(nums)/2
    count = Counter(nums)
    if n < len(count):
        return n
    else:
        return len(count)
    