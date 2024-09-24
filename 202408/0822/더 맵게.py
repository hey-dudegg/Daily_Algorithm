""" 10분까지 읽고 아이디어 생각해보기
- new_scov = min1 + min2*2
- 모든 음식의 scov >= K
- 몇 번이나 음식 조합을 반복해야할까?

- 입력: scoville 음식리스트 / K 최소 스코빌지수
- 출력: 모든 음식이 scoville 지수 K이상이 되기위한 조합 횟수

반복 : 모든 음식이 K보다 클 때까지
  - 음식리스트를 정렬 -> min1, min2 
  - min1 < K
  - new_scov = min1 + min2*2
  - new_scv -> 음식리스트

항상 정렬하는 대신 -> 음식 리스트를 Heap구조로 유지해서 min을 빠르게 찾아내자!


종료 조건: len(scoville) == 1
 -1

"""
import heapq

def solution(scoville, K):
    
    heap = []
    for scov in scoville:
        heapq.heappush(heap, scov)
    
    answer = 0
    # 반복해서 최소값을 꺼낸다. min1과 min2를 꺼내서 계산해서 다시 힙에 push한다.
    while heap[0] < K:
            # 예외 처리
        if len(heap) == 1:
            return -1

        answer += 1
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)

        new = min1 + (min2 * 2)

        heapq.heappush(heap, new)
        
    else:
        return answer
    
    
    