'''
[[복습]]

문제 이해
- (로 열렸으면, 반드시 동일한 갯수의 )로 닫혀야 한다.

- 입력 : 잘 닫혔는지 모를 () 문자열
- 출력 : 잘 닫혔다면 true, 아니라면 false

문제 정의
- ( -> +1, ) -> +0으로 생각한다.
- cnt를 0으로 세고, -1이 되면 false 반환.

- 문자열을 처음부터 탐색한다.
 - 만약 cnt가 음수라면
  - return false
 - 아니라면
  - ( -> +1, ) -> -1
  
 - if cnt != 0:
  - return false
 - else:
  - return true


제한 사항
n = 100T
O(n^2) 불가
)로 시작하는 상황 불가, (이 시작점이다.

느낀점
반드시 스택을 사용해야 하는 것이 아니라, 스택의 원리를 활용해 리스트로 푸는 것이다.

'''

def solution(str):
    
    cnt = 0
    
    for c in str:
        if cnt < 0:
            return False
        else:
            if c == '(':
                cnt += 1
            else :
                cnt -= 1
    
    if cnt == 0:
        return True
    else :
        return False


"""
문제 이해
- 올바른 괄호 -> ()의 짝이 맞음
- 올바르지 않은 괄호 -> 닫히는 괄호로 시작 or 열린 괄호가 닫히지 않거나

- 출력: 올바른 괄호 여부 [Bool]

아이디어
- Stack
 - "열린 괄호"를 만나면 push
 - "닫힌 괄호"를 만나면 pop
  - "닫힌 괄호"로 시작: 반복이 종료되었는데 
 
 - answer = isEmpty()
 - case
  - ()()
    stack = [ :
  - (())()
    stack = [ :
  - )()(
    stack = [ ( :

제한사항
- s: 100,000 100K
- O(n^2) = 100M


"""

def solution(s):
    stack = []
    
    for pa in s:
        if pa == "(":
            stack.append("()")
        else:
            if not stack:
                return False
            stack.pop()

    if stack:
        return False
    
    return True