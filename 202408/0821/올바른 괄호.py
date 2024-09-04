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