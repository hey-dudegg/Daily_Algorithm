"""
문제 이해
- 0부터 9까지 이루어진 배열이 주어짐
- 연속된 숫자는 하나만 남기고 제거
- 입력: 숫자 [리스트]
- 출력: 연속이 제거된 [리스트]

아이디어
- 스택 필요함
- arr을 반복 조회[순회]
 - if 스택에 현재 쌓여있는 요소의 값과 다르면 push
 - peek != arr -> push
 
제한 사항
-arr: n: 1M
- O(n)

"""
def solution(arr):
    answer = [] # 스택
    
    for ar in arr:
        if not answer:
            answer.append(ar) # push
        else:
            if answer[-1] != ar: # peek != value
                answer.append(ar) # push
                
    return answer