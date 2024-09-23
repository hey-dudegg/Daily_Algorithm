'''
[[복습]]
문제 이해
큐에서 프로세스를 빼는데, 대기큐 안에 우선순위가 더 높다면 다시 넣는다.
우선순위가 가장 높다면, 그대로 빠진다.
순서 지킨다.(큐 사용)

입력 : 우선순위 리스트, 알고싶은 숫자의 순서
출력 : 해당 순서의 실행 순서

문제 정의
- 완전 탐색 두번 한다.
- 순서를 알기 위한 cnt 순서 정의

- dequeue한다.
- dequeue한 값과 리스트의 모든 숫자와 비교한다.
 - 값이 큰 값이 있다면 다시 enqueue한다.
- 없다면
 - continue
 - cnt + 1

return cnt

제한 사항
N = 100
O(n^2) = 10T
O(n^3) = 1M

느낀점
현재의 것을 맨 뒤로 빼고, 자신보다 우선순위가 높은 큐들을 계속 삭제하고 그 숫자를 세면 된다.
 -> 큐의 원리를 활용하면 됨.
from collections import deque
que = deque() -> 디큐 선언
enumerate() -> 새 정렬된 리스트를 반환합니다.
pop(), popleft() -> 삭제
append(), appendleft() -> 삽입
any() -> 하나라도 true면 true

'''
from collections import deque

def solution(priorities, location):
    # [2, 1, 3, 2]
    # [0:2, 1:1, 2:3, 3:2]
    
    # 큐 채우기
    queue = deque([]) # (loc, pri)
    for loc, pri in enumerate(priorities):
        queue.append((loc, pri))
    

    # - queue에서 프로세스 하나 꺼내기 (dequeue)
    # - 대기중인 queue 조회
    #   - 우선순위가 높은 프로세스가 있으면 (enqueue)
    #   - 없으면 실행하기  
    # - location에 해당하는 프로세스가 몇번째로 실행되는지 확인하기
    
    order = 0
    
    while queue:
        cur = queue.popleft()
        
        if any(cur[1] < q[1] for q in queue):
        # if cur_priority < max(queue_priority):
            queue.append(cur)
        else:
            order += 1
            if cur[0] == location:
                return order



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