def solution(s):
    cnt = 0
    
    for pth in s:
        if pth =='(':
            cnt += 1
        else:
            cnt-=1
            if cnt < 0:
                return False
    if cnt > 0 :
        return False
        
    return cnt == 0
