def solution(n):
# 문제 이해 -> 문제 입출력, 특이점
# 입력 -> n
# 출력 -> n의 약수의 총합
# 약수 -> n으로 나누었을 때 나머지가 0이 되는 수
# 제한 사항 -> 시간복잡도 및 제한사항
# n <= 3000
# O(n) = 3K
# O(n^2) = 3k * 3k = 9M 
# 아이디어 -> 의사코드
# - answer 초기화하기
    answer = 0
# - n만큼 반복(1 - n)
    for i in range(1, 1+n):
#  - 만약 n을 나눈 나머지가 0인 경우 값 더하기
      if n % i == 0:
            answer += i
    return answer

# 아이디어2 :
# - 약수의 합을 만들려고 하면
# - 약수를 찾아서 더한다
# - 100
# - 1, 100
# - 2, 50
# - 4, 25
...
import math
math.sqrt() # 루트를 구할 수 있다.

# - sqrt를 찾는다.
# - sqrt만큼 반복한다.
#  - 만약에 나머지가 0인 경우, i, i//i를 더한다.
#   - i, n//i가 같은 경우 i를 한번 뺀다.
# O(n) -> O(log n)
sqrt = int(math.sqrt(n))
for i in range(1, 1+sqrt): # 가독성을 위해 1부터 시작
    answer += i
    answer += n//i
    if i*i == n:
        answer -= i
    

def solution(n):
    # 문제 이해
    # 입력 - 3000 이하 정수 n
    # 출력 n의 약수를 모두 더한 값
    
    # 아이디어
    # - sqrt를 이용하여 n의 제곱근을 구한다.
    import math
    sqrt_n = int(math.sqrt(n))
    # - sum = 0
    sum = 0
    # - 1부터 n의 제곱근 포함까지 반복한다.
    for i in range(1, 1 + sqrt_n):
        if n % i == 0:
            sum += i
            sum += n / i
            if i == sqrt_n:
                sum -= i
    #  - 만약 n을 i로 나눈 값이 0이라면(약수라면)
    #   - i와 n//i를 sum에 더한다.
    #   - 만약 i이 sqrt와 같다면, sum에서 중복되는 i를 한번 빼준다.
    
    # 제한사항
    # O(n^2) = 9M
    return sum