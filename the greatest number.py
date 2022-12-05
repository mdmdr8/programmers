# 가장 큰 수

def solution(numbers):
    numbers = [str(num) for num in numbers]
    numbers.sort(key=lambda x : x*3, reverse=True)
    return str(int(''.join(numbers)))
    

#Study

- numbers 정수를 str형으로 치환한 뒤, 리스트로 변환
- x*3을 하는 이유는, numbers 인자 각각의 문자열을 3번 반복한다는 뜻이다. [999, 555, 343434, 303030, 333]
  numbers는 1000이하의 숫자이므로 최대값을 생각해 3을 곱하고, 정렬하면 [999, 555, 343434, 333, 303030]

