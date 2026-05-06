def solution(participant, completion):
    # participant : 참가자들 (1~100000 / len(이름) : 1~20 알파벳 소문자, 동명이인 존재가능) 
    # completion : 완주자들
    # 목표 answer : 완주하지 못한 선수 이름을 return
    answer = ''
    dic = {}
    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i]=1
    for i in completion:
        dic[i]-=1
    for name, n in dic.items():
        if n>0:
            return name
