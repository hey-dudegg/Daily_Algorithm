def solution(nums):
    # 문제이해
    # 입력 : 1차원 리스트, 길이는 10,000이하 자연수의 짝수, 종류번호는 1-200,000
    # 출력 : 선택할 수 있는 포켓몬 종류 개수의 최댓값 하나
    
    # 아이디어
    # 리스트를 집합(set)에 담으면 중복 제거.
    # 집합의 크기 반환
    
    # 제한사항
    
    
    # 문제이해
    # - N개가 주어짐 -> N/2를 선택하는 문제
    # - N에 중복된 요소가 있을 수 있고
    # - 최대한 중복되지 않는 N/2를 찾는 문제
    # - 입력 : 폰켓몬 리스트
    # - 출력 : 내가 고른 폰켓몬 종류의 수
    
    # 아이디어
    # - 일단 중복되지 않게 고른다
    # - 중복되지 않게 고른 후에는 아무거나 골라도 됨
    # 중복되지 않는 폰켓몬 리스트를 만들기(unique)
    # - unique의 수와 n/2과 비교
    #  - unique > n/2: n/2 선택
    #  - n/2 > unique: unique 선택
    
    # 제한사항
    # - n: 10,000 -> 10K
    # O(n^2) -> 10K*10K -> 100M
    
    answer = 0
    
    # 중복없는 폰켓몬 리스트 만들기
    # uniq = set(nums)
    uniq = []
    for n in nums:
        if n not in uniq:
            uniq.append(n)
            
    selection = len(nums)//2
    uniq_cnt = len(uniq)
    
    if selection > uniq_cnt:
        answer = uniq_cnt
    else:
        answer = selection
    
    return answer