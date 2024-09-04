"""
문제 이해
- 최고의 집합: 원소의 합이 S / 원소의 곱이 최대
- 입력: n 원소의 수 / s 원소의 합
    
아이디어
- s를 n개의 원소로 나누었을 때, 원소가 거의 비슷한 값을 가져야 곱이 최대가 됨
- s를 n으로 나눈 몫으로 모든 집합을 채우고, 나머지를 1씩 분배하기
  - n: 3, s: 10
  - 10//3 -> 3 ; 10%3 -> 1
  - 3, 3, 3 > 4, 3, 3
- 합이 n보다 작은 경우; n=2, s=1인 경우 존재하지 않음
- 정렬하기
"""
def solution(n, s):
    if s < n:
        return [-1]
    
    # 기본 값으로 몫을 모든 원소에 채우기
    quotient = s // n
    remainder = s % n
    
    # 기본 값을 리스트에 넣고, 나머지를 분배
    answer = [quotient] * n
    
    for i in range(remainder):
        answer[i] += 1
    
    # 오름차순 정렬하여 반환
    answer.sort()
    
    return answer