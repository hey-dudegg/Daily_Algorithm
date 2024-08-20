def solution(numbers):
    #ver1.
#    checker = [0]*10 # 등장 여부를 업데이트
    
#    for num in numbers:
#        checker[num] += 1
        
        
#    answer = 0
#    for idx, chk in enumerate(checker):
#        if chk == 0:
#            answer += idx
 
    full_set = {0, 1,2,3,4,5,6,7,8,9}
    numbers = set(numbers)
    diff = full_set.difference(numbers)
            
    return answer
