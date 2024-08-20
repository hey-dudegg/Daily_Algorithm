def solution(s):
    # 영어로 바뀌었거나, 바뀌지 않은 문자열 s 입력
    # s가 의미하는 원래 숫자 출력
    
    # 파싱해야 할듯, 파싱하면서 첫 문자를 보고 경우의 수에 맞는 if문 작성
    # ans 문자열
    result = ""
    tmp = ""
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    # 0부터 s의 길이까지 반복문
    for c in s:
        if c.isnumeric():
            result += c
        else:
            tmp += c
            if tmp in arr:
                result += str(arr.index(tmp))
                tmp = ""
                
    ans = int(result)
    # - 'z'라면 ans에 0 append 후 i를 +3
    # - 'o'라면 1 append 후 i를 +2
    # - 't'라면
    #  - i+1번째가 w라면 +2
    #  - h라면 +4
    # - 'f'
    #  - 'o' +3
    #  - 'i' +3
    # - 's'
    #  - 'i' +2
    #  - 'e' +4
    # - 'e' +4
    # - 'n' +3
    
    # 0으로 시작X, 50이하.
    
    return ans
