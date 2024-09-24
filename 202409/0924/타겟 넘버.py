"""dfs; 15분까지 읽어보기
- 입력:
  - numbers: [리스트] 숫자
  - target: 만들어야하는 숫자
- 출력: 숫자를 만들 수 있는 가짓수

- 아이디어 각 노드가 + / -의 엣지를 갖는 트리라고 생각할 수 있지 않을까?
0: [0] -> 2
4: [0+4]               [0-4]
1: [0+4+1] [0+4-1]     [0-4+1] [0-4-1]
2: [0+4+1+2] [0+4+1-2]
1: [0+4+1+2+1]
r(4):  0 0  0 1 0 1 0 0 0 0 0 0 0 0 
"""

def dfs_number(numbers, index, target, cur_sum):
    if index == len(numbers):
        if cur_sum == target:
            return 1
        else:
            return 0
    
    add_sum = cur_sum + numbers[index]
    add_case = dfs_number(numbers, index+1, target, add_sum)
    
    sub_sum = cur_sum - numbers[index]
    sub_case = dfs_number(numbers, index+1, target, sub_sum)
    
    return add_case + sub_case
    
def solution(numbers, target):
    answer = dfs_number(numbers, 0, target, 0)
    
    return answer