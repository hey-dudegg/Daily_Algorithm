########################################
## 백준 2941 크로아티아 알파벳
# 크로아티아 알파벳을 인코딩하지 못하여 알파벳으로 변경하여 쓰던 시절이 있었습니다.
# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력하세요.

## 풀이
# 인코딩 표를 보니, 문자 7개와 특수문자는 3개로 변경될 수 있다는 걸 봤습니다.
# 이를 switch 문을 통해 해결할 생각입니다. (switch문은 파이썬에 없으므로 if~elif로 대체)
# 또한 특수문자의 여부는 반복되기 때문에, 함수화 시켜서 활용하겠습니다.

## 남의 코드 요약
# 
########################################
s = input()
idx = [0]
cnt = [0]

def is_croatic (c) :
    if c == "l" or c == "n" :
        if s[idx[0] + 1] == "j" :
            return 1
        
    elif c == "d" :
        if idx[0] + 1 == len(s) :
            cnt += 1
            return 0
        return 1

    elif s[idx[0] + 1] == "=" or s[idx[0] + 1] == "-" :
        return 1
    
    else :
        return 0
        
for i in s :
    if i == "=" or i == "-":
        idx[0] += 1
        cnt[0] += 1
        continue

    if idx[0] + 1 < len(s) :
        if i == "c" or i == "d" or i == "l" or i == "n" or i == "s" or i == "z" :
            if is_croatic(i) :
                idx[0] += 1
                continue
        else :
            idx[0] += 1
            cnt[0] += 1
    else :
        idx[0] += 1
        cnt[0] += 1
               
print(cnt[0])
