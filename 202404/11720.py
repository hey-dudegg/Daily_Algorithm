####################################
## 소개
# 백준 11720 숫자의 합
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
# 입력으로 주어진 숫자 N개의 합을 출력한다.

## 풀이
# 띄어쓰기 없이 입력되는 숫자를 파싱해서 배열에 저장한다.
# 배열의 인덱스를 더한 sum을 출력한다.
#####################################
# import sys

# input = sys.stdin.readline()
# num = int(input)
# sum = 0
# input2 = sys.stdin.readline()

# for i in range(num):
#     sum += int(input2[i])

# print(sum)

#######################
# 다른 사람 것
k = 0
N = input()
for i in input():
    k += int(i)
print(k)