def solution(com):
    answer = 0
    num = com[1]-com[0]
    n = len(com)
    if com[1]+num == com[2]:
        answer = com[0]+(n*num)
    else:
        d = com[1]//com[0]
        answer = com[0]*(d**n)
    return answer