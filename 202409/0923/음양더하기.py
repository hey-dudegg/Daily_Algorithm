""" 40분까지 직접 문제 풀어보기
- absolutes: 정수의 절대값
- signs: 부호 ; True 양수 / False 음수

- result: signs를 적용한 absolutes의 총합
"""
def solution(absolutes, signs):
    answer = 0
    # for i in range(len(absolutes)):
    #     if signs[i]:
    #         answer += absolutes[i]
    #     else:
    #         answer -= absolutes[i]
    
    for value, sig in zip(absolutes, signs):
        if sig:
            answer += value
        else:
            answer -= value
            
    return answer