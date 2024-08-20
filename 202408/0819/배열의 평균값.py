def solution(numbers):
    # 문제 이해
    # 입력 : 리스트
    # 출력 : 리스트 요소 합의 평균값
    
    # 아이디어
    # - 리스트를 전체 탐색
    #  - 모든 값을 더한다.
    #  - cnt 값도 올려준다.
    # ans = 모든 값 / cnt
    length = len(numbers)
    cnt = 0
    num_sum = 0
    
    for i in range(0, length):
        num_sum += numbers[i]
        cnt += 1
    answer = num_sum / cnt
    
    # 제한 사항
    # n <= 100
    # O(n^2) = 10K
    return answer