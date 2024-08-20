def solution(today, terms, privacies):
    # termsTable 만들기 {type:month}
    termTable = {}
    for t in terms:
        t = t.split()
        termTable[t[0]] = int(t[1])

    # 오늘날짜를 days로 바꾸기
    today_year, today_month, today_day = map(int, today.split("."))
    today2days = today_year * 12 * 28 + today_month * 28 + today_day

    answer = []
        
    # privacies를 반복하기
    for idx, prv in enumerate(privacies):
        date, term_type = prv.split()
        date_year, date_month, date_day = map(int, date.split("."))
        date2days = date_year * 12 * 28 + date_month * 28 + date_day 
        exp_day = date2days + termTable[term_type] * 28 
        # 개인정보 수집일자 + 유효기간을 오늘날짜랑 비교하기
        if exp_day <= today2days:  # 오늘 날짜와 비교
            answer.append(idx + 1)  # 오늘보다 이전이면 파기가 필요한 것으로 확인 (1부터 시작하는 인덱스)
    
    return answer



'''
문제 이해
- 모든 달은 28일까지
- 개인정보 타입별로 유효기간이 다름
- 유효기간이 지나면 파기해야함

- 입력
 - today: 오늘날짜 -> yyyy.mm.dd
 - terms: 약관별 유효기간 -> "약관 타입 v 유효기간(개월)" [리스트]
 - privacies: 동의한 약관들 -> "동의날짜 v 약관 타입" [리스트]
 
- 출력
 - 파기해야하는 약관의 번호
 
- 약관 번호를 1 ~ n으로 사용해야함

아이디어
- 약관 종류랑 유효기간을 저장할 수 있는 공간(termsTable) {type:month}
- 개인정보 수집일자 + 유효기간 < 오늘 : 파기
- 출력하기
** 연월일 -> 일
 - 1년 : 12개월 * 28일
 - 1개월 : 28일
 - "일"

제한사항
- terms: 20 n
- privacies: 100 m

'''