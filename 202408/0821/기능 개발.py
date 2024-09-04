"""
문제이해
- 입력: 
  - progresses: 현재 작업의 진행상황 [리스트] 숫자
  - speeds: 각 작업의 수행 속도 [리스트] 숫자
- 출력:
  - 배포가 일어날 때 배포되는 기능의 수

아이디어
- 1기수마다 progresses의 현황을 업데이트하기 (speed 만큼)
- 배포 가능한 기능 배포하기 (queue)
  - 배포된 기능이 있다면 숫자세서 추가하기

제한사항
- n: 100
"""

# from collections import deque # queue를 사용하기 위해 deque 가져오기

def solution(progresses, speeds):
    # - 1기수마다 progresses의 현황을 업데이트하기 (speed 만큼)
    # - 배포 가능한 기능 배포하기 (queue)
    # - 배포된 기능이 있다면 숫자세서 추가하기
    answer = []
    # progresses = deque(progresses)
    # speeds = deque(speeds)
    
    while progresses: # 모든 작업이 완료될 때까지 반복
        # 작업상태 업데이트
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] > 100:
                progresses[i] = 100
            
        cnt = 0
        
        while progresses and progresses[0] == 100: # peek
            progresses.pop(0) # dequeue
            speeds.pop(0)
            cnt += 1
        
        if cnt > 0:
            answer.append(cnt)
            
    return answer