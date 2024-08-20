def solution(n):
    # 문제 이해
    # 입력 : N 자연수
    # 출력 : N 자릿수의 합

    # 아이디어
    # 숫자를 입력받아서 -> 문자로 치환
    # 123 -> "123"
    # 문자 기준으로 반복하면서 자릿수 더하기

    # 제한사항
    # N -> 100M
    # O(N) 100M
    # O(log n) 100M-> 9
    
    answer = 0
    string = str(n) # 문자로 변환

    for c in string:
        answer += int(c)
        
    # 10으로 나누면서 풀기
    # n
    # 반복 n이 0이 될 때까지
    # - n % 10을 더하기
    # - n을 n // 10으로 업데이트
        
    return answer