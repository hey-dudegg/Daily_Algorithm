def solution(a, b):
    # 문제 이해
    # 입력으로 a,b 숫자(1-6)
    # 출력 : 점수
    # - 둘 다 홀수일 때
    # - 하나만 홀수일 때
    # - 홀수가 없을 때
    
    # 아이디어
    # - 홀수 여부 파악하기
    # - 조건에 따라 점수 계산하기
    
    # 제한사항
    # a, b : 6
    # O(1)
    
    answer = 0
    
    a_odd = a % 2 # 홀수이면 1, 짝수이면 0
    b_odd = b % 2
    
    if a_odd == 1 and b_odd == 1:
        answer = a**2 + b**2
    elif a_odd == 1 or b_odd == 1:
        answer = 2*(a+b)
    else:
        answer = abs(a-b)
        
    
    return answer