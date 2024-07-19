############################
## 2747 피보나치 수(1)
# 첫째 줄에 45보다 작거나 같은 자연수인 n이 주어집니다. 
# 이에 n번째 피보나치 수를 출력하는 문제입니다.

## 입력
# 첫째 줄에 n이 주어진다. n은 45보다 작거나 같은 자연수이다.

## 출력
# 첫째 줄에 n번째 피보나치 수를 출력한다.

## 풀이
# 반복문을 활용, 재귀함수 활용, DP를 활용한 3가지 풀이 방법이 있습니다.
############################

import sys
import time

input = sys.stdin.readline
n = int(input())
start = time.time()

## 반복문
# a, b = 0, 1
# for i in range(n):
#     a, b = b, a + b

## 재귀문
# def recursion_fibo(n):
#     return 1 if n <= 2 else recursion_fibo(n - 2) + recursion_fibo(n - 1)

## DP 활용
def dp_fibo(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp[n]

print(f"n이 {n}일 때 :")
# print(f"Fibonacci Result: {a}, Time: {time.time() - start:.16f} sec")
# print(f"Fibo_Recur Result: {recursion_fibo(n)}, Time: {time.time() - start:.16f} sec")
print(f"Fibo_DP Result: {dp_fibo(n)}, Time: {time.time() - start:.16f} sec")