def solution(arr, com):
    answer = []
    # com에서 한개씩 배열을 꺼내고 
    # 그 배열 안에서 인덱스 0과 1까지 숫자를 꺼내 arr를 slice한다. for문으로
    # 정렬 .sort()
    # com[2] 번째를 arr의 n번째 인덱스의 숫자를 가져와 answer에 저장
    for i in range(len(com)):
        array = arr[com[i][0]-1: com[i][1]]
        array.sort()
        answer.append(array[com[i][2]-1])
    return answer
    
    
 # 다른 사람 풀이 1
def solution(arr, coms):
  answer = []
  for com in coms:
      i,j,k=com
      answer.append(sorted(arr[i-1:j])[k-1])
  return answer
         
# 다른 사람 풀이 2

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
