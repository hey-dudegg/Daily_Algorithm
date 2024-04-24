#################################
## 백준 1316 그룹 단어 체커
# 그룹 단어란, 단어에 존재하는 모든 문자에 대해서 각 문자가 연속해서 나타나는 경우만을 말합니다.
# 단어 N개를 입력 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하세요.

## 풀이
# 단어를 입력받아 배열에 넣습니다.
# 이후 배열에 문자가 존재한다면 같은지 확인합니다.
# 같다면 continue하고, 다르면 break합니다.

## 남의 코드
# 
#################################
n = int(input())

arr = [] * n
cnt = n

for i in range(n) :
    str = input()
    tmp = [] * len(str)

    for j in range(len(str)) :
        if str[j] not in tmp :
            tmp.append(str[j])
        elif str[j] == str[j - 1] :
            continue
        else :
            cnt -= 1
            break
print(cnt)
        