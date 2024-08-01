#####################################
## 2798 블랙잭
# 블랙잭은 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임입니다.
# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구하는 문제입니다.

## 입력
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

## 출력
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

## 풀이 과정
# 1. 완전탐색의 방법으로, 3개의 반복문을 활용합니다.
#  - 수학에서의 조합 개념과 같이, 3개의 숫자를 리스트에 담아 첫 반복문에서는 리스트의 첫 요소부터 n-2개까지,
#  - 두번째 반복문은 첫 반복문의 i보다 큰 수부터 n-1까지, 세번째 반복문은 i+2부터 n-2까지
#  - for i in range(1, m-2), for j in range(i+1, m-1), for k in range(i+2, m-2)
# 2. 변수 N,M을 입력받고, 나머지 N개의 숫자들을 리스트에 append합니다. M을 넘지않는 숫자 max를 초기화한 뒤, 수를 더하며 업데이트합니다.
#####################################

import sys

# 입력값을 받고 파싱합니다. 변수를 선언합니다.
input = sys.stdin.readline().split()
n, m = map(int, input[:2])
input = sys.stdin.readline().split()
num_list = list(map(int, input))
max = -1

# 입력받아 리스트에 저장한 값을 완전 탐색합니다.
for i in range(0, n-3):
    for j in range(i+1, n-2):
        for k in range(i+2, n-1):
            tmp = 0
            tmp = num_list[i] + num_list[j] + num_list[k]
            if max < tmp <= m:
                max = tmp
            # print(f"i: {i}, {num_list[i]}, j: {j}, {num_list[j]}, k: {k}, {num_list[k]}, tmp = {tmp}, max = {max}")
            if max == m:
                break
print(max)