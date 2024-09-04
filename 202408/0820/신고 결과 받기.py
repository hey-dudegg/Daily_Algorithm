"""
문제 이해
- 입력
 - id_list : 유저의 목록[리스트]
 - report: 유저가 신고한 목록 [리스트]
 - k: 
 - 한 사람이 한명을 여러번 신고할 수는 없음(중복 불가)
 - 신고가 모두 완료된 후에 정지 메일을 받음

아이디어
- 신고 받은 사람의 신고 횟수
- reporter가 신고한 사람 중에 정지당한 사람의 수 세기

제한 사항
- id_list: n: 1,000 1K
- report: 200,000 200K
- O(n*M) = 1K * 200K = 200M

"""

def solution(id_list, report, k):
    answer = []
    # reportTable: {신고 당한 사람: [신고한 사람]}
    reportTable = {}
    for id in id_list:
        reportTable[id] = []
        
    # reportTable 채우기
    for rep in set(report):
        reporter, reported = rep.split()
        reportTable[reported].append(reporter)
    
        
    # 신고 당한 사람이 unique하게 몇번 신고당했는지 확인
    # bannedTable: 유저리스트 -> 누가 정지됐는지 확인하는 테이블
    
    bannedTable = {} # {신고 당한 사람:신고 여부(True/False)}
    for id in id_list:
        if len(reportTable[id]) >= k:
            bannedTable[id] = True
        else:
            bannedTable[id] = False
    
    #  - k랑 비교
    # id_list를 기준으로 내가 신고한 사람 중에 몇명이나 정지됐는지 확인
    mailCntTable = {} # {신고한 사람: 받은 메일 수}
    for id in id_list:
        mailCntTable[id] = 0
        
    for reported, reporters in reportTable.items():
        if bannedTable[reported]:
            for rep in reporters:
                mailCntTable[rep] += 1
    
    for id in id_list:
        answer.append(mailCntTable[id])
    
    return answer