#############################################
## 백준 2439 별찍기-2
# 첫째 줄에 별 1개, 둘째 줄에 별 2개 ... N번째 줄에는 별 N개를 찍는 문제입니다.
# 오른쪽을 기준으로 정렬한 별을 출력하세요.

## 문제 풀이
# N번만큼 반복하는 반복문을 작성합니다.
# 공백은 N - i개씩 출력되고, 별표는 i개 만큼 반복되면 완성
#
## 실수한 점
# print문은 한 줄을 작성한다. 나는 print 문을 두 개 적어서 두 줄로 출력됐다.

n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)