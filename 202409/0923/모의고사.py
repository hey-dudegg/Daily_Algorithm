"""27분까지!
문제이해
- 수포자!
- #1: 1, 2, 3, 4, 5 반복
- #2: 2, 1, 2, 3, 2, 4, 2, 5 반복
- #3: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 반복

- 출력: 가장 높은 점수를 받은 사람 리스트

아이디어
- Brute Force!!!!!
- 문제랑 답이랑 다 비교하자!!!!!!
  - 패턴에 따라 답을 내니까 -> 문제번호 % 패턴 수 => 어떻게 답했는지 확인

n: 10,000 10K
O(n^2) -> 100M
"""
def solution(answers):
    supo = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    
    dap = [0] * 3
    
    for i in range(3):
        for idx, ans in enumerate(answers):
            if answers[idx] == supo[i][idx % len(supo[i])]:
                dap[i] += 1
    
    max_score = max(dap)
    highest = []
    for i, high in enumerate(dap):
        if max_score == dap[i]:
            highest.append(i+1)
            
    highest.sort()
    
    return highest
