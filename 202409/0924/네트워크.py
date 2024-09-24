""" 10분까지
- 연결되어있는 노드들끼리는 같은 네트워크다!
- 주어진 데이터에서 네트워크는 몇개?

- DFS 탐색을 시작!
- 탐색이 완료된 후에도 방문되지 않은 노드가 있다면, 서로 다른 네트워크에 위치

- computer: 2차원 -> 인접 행렬

** DFS는 완전탐색을 진행하니까 DFS를 완료하고나면 연결된 모든 노드를 방문한 상태가 된다.
"""

def dfs_network(computer, start, visited):
    visited[start] = True
    for i in range(len(computer[start])):
        if not visited[i] and computer[start][i] == 1:
            dfs_network(computer, i, visited)
    

def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    for i in range(n):
        if not visited[i]:
            dfs_network(computers, i, visited)
            answer += 1
    
    return answer