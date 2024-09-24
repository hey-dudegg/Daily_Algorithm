"""
- 금요일: 순열(permutations)을 활용한 완전 탐색
- 오늘: DFS를 활용해서 완전 탐색

- graph: 모든 던전이 연결되어있는 그래프라고 생각하자
- dfs -> 가장 깊숙히; 더 이상 들어갈 수 없을 때까지 던전을 방문하고 입장 횟수의 최댓값 찾기

- 종료 조건 -> 더 이상 들어갈 던전이 없거나 남은 던전의 최소 피로도가 현재 피로도보다 높다.

"""
def dfs_dungeons(k, dungeons, visited, cnt):
    max_count = cnt
    
    for i in range(len(dungeons)):
        req, con = dungeons[i]
        if not visited[i] and k >= req: # 다음 뎊스로 들어갈 수 있는 조건
            visited[i] = True
            new_count = dfs_dungeons(k-con, dungeons, visited, cnt+1)
            max_count = max(max_count, new_count) # 같은 레벨의 다른 결과들과 최대값 비교
            visited[i] = False # 백트래킹을 위해 방문 철회

    return max_count
    
def solution(k, dungeons):
    answer = -1
    
    visited = [False]*len(dungeons) # 방문여부를 저장하기
    answer = dfs_dungeons(k, dungeons, visited, 0)
    
    return answer