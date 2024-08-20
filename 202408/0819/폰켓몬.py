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

def solution(nums):
    # 입력 : 1차원 리스트
    # 출력 : 가장 많은 종류의 폰켓몬 선택
    # 최대 선택 갯수 구하기
    # 중복되는 종류 없애기(집합)
    answer = 0
    set_nums = set(nums)
    # 만약 최대 갯수보다 종류가 많다면 -> 종류
    if len(nums)/2 < len(set_nums):
        answer = len(nums)/2
    # 종류가 최대 갯수보다 많다면 -> 최대 갯수
    else:
        answer = len(set_nums)
    
    # O(N^2) = 100M
    
    return answer