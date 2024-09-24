""" 
다익스트라 알고리즘: 최단경로 탐색 활용
- 마을이랑 마을 사이의 소요시간(경로)가 주어지고
- 주어진 제한시간 K 안에 배달할 수 있는 마을의 숫자를 찾는 문제

- 입력
  - N: 마을 갯수 -> Node의 수
  - road: 경로 정보 -> Edge의 정보
  - K: 제한 시간
 - 출력
  - 기준마을 1번으로 부터 소요시간이 K 이하인 마을의 수
    
    자료구조 초기화
    # 경로가 저장되어있는 그래프
    # 각 노드까지 거리를 저장할 공간
    # 그래프를 순회할 큐
    
    다익스트라 알고리즘 수행
    -> distance 완성
    
    K 이하인 마을의 수 세기
    -> distance에서 조회

"""

from collections import deque

def solution(N, road, K):
    # 자료구조 만들기
    
    # 그래프 만들기 # 인접 리스트
    # N+1개의 빈 리스트 만들어짐
    graph = []
    for i in range(N + 1):
        graph.append([])
    
    for a, b, c in road: # from, to, dist
        graph[a].append((b, c)) # (node, dist)
        graph[b].append((a, c))
        # 방향성이 없으므로 양쪽 전부 더하기
    
    # 노드까지 거리를 저장
    distance = [float("inf")] * (N+1)
    distance[1] = 0 # 기준점 1번 노드
    
    # graph를 순회할 queue
    queue = deque([])
    queue.append((1, 0)) # node, dist # 1번 노드를 입력
    
    # 다익스트라 알고리즘을 실행!
    while queue:
        cur_node, cur_dist = queue.popleft()
        
        for node, dist in graph[cur_node]:
            new_dist = cur_dist+ dist
            if distance[node] > new_dist:
                distance[node] = new_dist
                queue.append((node, distance[node]))
                             
    # 문제 조건에 맞게 결과 출력
    answer = 0
    for d in distance:
        if d <= K:
            answer += 1
    
    return answer