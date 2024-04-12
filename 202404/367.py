#################################
## 백준 1269 
# 자연수를 원소롤 갖는 공집합이 아닌 두 집합 A와 B가 있다.
# 두 집합의 대칭 차집합의 원소의 개수를 출력하는 프로그램을 작성하시오.

## 풀이
# 파이썬의 자료형인 set을 이용하여 두 집합을 합치면, 중복되는 정수는 제거되므로 그 set의 원소 개수를 세면 된다.
#################################
# import sys

# n, m = map(int, sys.stdin.readline().split())
# nums = set(map(int, sys.stdin.readline().split()))
# mums = set(map(int, sys.stdin.readline().split()))
# sums1 = nums - mums
# sums2 = mums - nums
# print(len(sums1) + len(sums2))

## 다른 사람
input()
a = set(input().split())
b = set(input().split())
print(len(a - b) + len(b - a))