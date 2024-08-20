def solution(players, callings):
    # - rank 딕셔너리 만들기 { 플레이어 이름: 인덱스}
    ranks = {}
    for idx, player in enumerate(players):
        ranks[player] = idx
    # - calling 만큼 반복
    for call in callings:
        cur_rank = ranks[call]
        tar_rank = cur_rank - 1
        tar_player = players[tar_rank]
        
        players[cur_rank], players[tar_rank] = players[tar_rank], players[cur_rank]
        
        ranks[call] = tar_rank
        ranks[tar_player] = cur_rank
    #  - rank[player] : 선수의 순위를 찾기
    #  - 선수의 순위를 앞선 순서랑 바꾸기
    #  - 바뀐 순서를 rank에 업데이트해주기
    
    return players


문제 이해
- 입력
 - players: 현재 순위 [리스트]
 - callings: 추월한 선수 이름 [리스트]
- 출력
 - result: 최종 순위 [리스트]

아이디어
- calling을 반복하기
 - calling에서 불려진 선수를 찾아서 앞의 선수랑 순서를 바꿔주면 됨
- 아이디어 : 불려진 선수를 쉽게 찾기 위해서 rank라는 딕셔너리 만들기
rank: {플레이어 이름: 인덱스(순위)}

제한사항
- n: players: 50,000 : 50k
- m: callings: 1,000,000 : 1M
- O(n*M) = 50K * 1M = 50G -> 아디이어가 필요
