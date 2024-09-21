"""
[[복습]]
문제 이해
- 배열 arr은 0-9
- 연속적인 숫자 하나만 남기고 제거
- 순서 유지해야.

- 입력 : arr
- 출력 : arr
문제 정의
- 스택 자료형을 준비한다.
- arr의 [0]번째를 stack에 push한다.
- arr을 반복 조회한다.
 - 앞에서부터 arr[i]번째가 stack의 peek 값과 동일한지 확인한다.
  - 동일하지 않다면 push한다.
  - 동일하다면 넘어간다.

제한 사항
- N = 1M
- N = O(n) 1M
- O(n^2) = 1T X

느낀점
- 스택의 원리를 활용해야겠다는 생각이 들었을 때, 반드시 스택 자료형을 사용할 필요는 없었습니다.
- 리스트를 활용하더라도 스택 자료형의 원리를 이용한다면 ok.

"""

def solution(arr):
    answer = []
    
    answer.append(arr[0])
    
    for ar in arr:
        if ar != answer[-1]:
            answer.append(ar)
    
    return answer











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