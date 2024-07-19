##############################
## 9095 1,2,3 더하기
# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있습니다. 
# 합을 나타낼 때는 수를 1개 이상 사용해야 합니다.
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 이처럼 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 문제입니다.

## 문제 풀이
# 반복문, 재귀문, DP를 활용해 풀이 가능합니다.
##############################

import sys
import time

n = int(sys.stdin.readline())
start = time.time()

## 반복문
# a, b, c = 1, 2, 4
# for _ in range(1, n):
#     a, b, c = b, c, a + b + c

## 회귀문
# def recur(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
#     else:
#         return recur(n - 1) + recur(n - 2) + recur(n - 3)

## DP
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    elif i == 3:
        dp[i] = 4
    else:
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    
print(f"n이 {n}일 때 :")
# print(f"Plus with loop: {a}, Time: {time.time() - start:.16f} sec")
# print(f"Plus with Recursion: {recur(n)}, Time: {time.time() - start:.16f} sec")
print(f"Plus with DP: {dp[n]}, Time: {time.time() - start:.16f} sec")