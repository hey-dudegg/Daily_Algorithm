"""
문제 이해
- queue에서 프로세스 하나 꺼내기 (deque)
- 대기중인 큐를 조회
 - 우선순위가 높은 프로세스가 있으면 (enqueue)
 - 없으면 실행하기
- location에 해당하는 프로세스가 몇번째로 실행되는지 확인하기

아이디어
- [A, B, C, D] - [2, 1, 3, 2]
 - A(2), [B, C, D] -> cnt + 1
- [B, C, D, A]
 - B(1), [C, D, A] -> 확인
- [C, D, A, B]
 - C(3), [D, A, B]
 - OK -> [C, D, A] ...
  - if 나오는 알파벳이 location에 해당하는 거면 CNT 반환
 
 - 입력
  - priorities: 숫자 [리스트]
  - location: 언제 실행되는지 궁금한 프로세스
  
 - 출력
  - location에 해당되는 프로세스가 실행되는 순서

제한사항
- priorities: n: 100
"""
from collections import deque
def solution(priorities, location):
    
    # [2, 1, 3, 2]
    # [0:2, 1:1, 2:3, 3:2]
    
    # 큐 채우기
    queue = deque([]) # (loc, pri)
    for loc, pri in enumerate(priorities):
        queue.append((loc, pri))
        
    order = 0
    
    while queue:
        cur = queue.popleft()
        
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            order += 1
            if cur[0] == location:
                return order