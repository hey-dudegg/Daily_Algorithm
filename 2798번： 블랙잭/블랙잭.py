#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2798                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: m5rep5wer <boj.kr/u/m5rep5wer>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2798                           #+#        #+#      #+#     #
#    Solved: 2024/08/12 15:07:29 by m5rep5wer     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

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

## 문제 해결
# 로직상 문제 없다고 판단했으나, 지속적으로 "틀렸습니다"를 출력했습니다. print문을 찍어본 결과, 탐색의 범위를 잘못 설정(i의 경우 n-2까지)하여
# 완전 탐색하지 못해 벌어진 문제였습니다.
# 실행 결과 : 31120KB / 88ms
# 함수형으로 개선 후 : 31120KB / 44ms
#####################################
# [함수형으로 개선]
import sys

# 입력값을 받고 파싱합니다. 변수를 선언합니다.
f_input = list(map(int, sys.stdin.readline().split()))
cards = list(map(int, sys.stdin.readline().split()))

# 입력받아 리스트에 저장한 값을 완전 탐색합니다.
def Nfor(arr, M):
    max = -1
    for i in range(0, f_input[0]-2):
        for j in range(i+1, f_input[0]-1):
            for k in range(j+1, f_input[0]):
                tmp = 0
                tmp = cards[i] + cards[j] + cards[k]
                if max < tmp <= M:
                    max = tmp
                # print(f"i: {i}번째 {num_list[i]}, j: {j}번째 {num_list[j]}, k: {k}번째 {num_list[k]}, tmp = {tmp}, max = {max}")
                if max == M:
                    return max
    return max
k = Nfor(cards, f_input[1])
print(k)

####################################################
# [기존 절차형 코드]
# import sys

# # 입력값을 받고 파싱합니다. 변수를 선언합니다.
# input = sys.stdin.readline().split()
# n, m = map(int, input[:2])
# input = sys.stdin.readline().split()
# num_list = list(map(int, input))
# max = -1

# # 입력받아 리스트에 저장한 값을 완전 탐색합니다.
# for i in range(0, n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             tmp = 0
#             tmp = num_list[i] + num_list[j] + num_list[k]
#             if max < tmp <= m:
#                 max = tmp
#             print(f"i: {i}번째 {num_list[i]}, j: {j}번째 {num_list[j]}, k: {k}번째 {num_list[k]}, tmp = {tmp}, max = {max}")
#             if max == m:
#                 break
            
# print(max)

######################################
## 다른 사람의 문제 풀이
# 1. 함수형 프로그래밍으로 작성하셨습니다. 저는 3중 for문으로 완전 탐색했습니다.
# 2. 반복문의 범위가 len(arr)까지로, 저는 3장만 뽑는다는 가정을 고려해 n-2까지 뽑습니다.
# 3. 왜 이 사람이 더 성능이 빠른것인지 모르겠습니다.
# 4. 31120Kb / 52ms
# import sys

# f_input = list(map(int,sys.stdin.readline().split()))
# cards = list(map(int,sys.stdin.readline().split()))

# # N는 뽑은카드수, M은 수의합, arr는 카드리스트
# def Nfor(arr,M): #3개뽑기에 3중포문으로만 가능함 왜냐면 첫번째 그리고 그다음인덱스 그리고 그다음인덱스 이런식으로 모든경우를 구하기때문
#     max =0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             for k in range(j+1, len(arr)):
#                 sum = arr[i]+arr[j]+arr[k]
#                 if sum<=M and sum>max:  # M보다는 작고 + max보다는 커야 계속 더 큰값이 들어감
#                     max = sum
#     return max
                                
# k =Nfor(cards,f_input[1])
# print(k)
