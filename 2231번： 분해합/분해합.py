#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2231                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: m5rep5wer <boj.kr/u/m5rep5wer>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2231                           #+#        #+#      #+#     #
#    Solved: 2024/08/13 11:01:14 by m5rep5wer     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
## 문제 풀이
# 1. 생성자를 찾기 위해 분해합의 각자릿수를 모두 더합니다.
# 2. 분해합에서 더한 값을 뺍니다. 
# 2-1. 탐색할 범위를 정하는데, 범위는 첫자릿수와, 자릿수-1만큼 9를 더한 값을 처음 분해자에서 뺀 값에서 시작합니다.
# 3. 뺀 값부터 완전탐색하며 찾습니다. 생성자로부터 분해합이 나오는지 찾습니다.
# 4. for문으로 찾으며 찾으면 break으로 빠져나오고 출력합니다.

## 성능
# 31120KB / 40ms

# import sys

# input_num_str = sys.stdin.readline()
# input_num = int(input_num_str)
# minus = 0

# if input_num > 9:
#     for i in range(len(input_num_str)-2):
#         minus += 9

# start_num = input_num - (minus + int(input_num_str[0]))

# for j in range(start_num, input_num):
#     digit_sum = 0
#     for k in range(len(str(j))):
#         digit_sum += int((str(j))[k])
#     sum = j + digit_sum
#     if sum == input_num:
#         print(j)
#         exit()
# print(0)

## 다른 사람 풀이
# max 함수를 사용해서 10 이하일 때 음수가 나오는 경우를 방지했습니다.
# 방식은 완전 탐색으로, 0부터 N까지 모두 탐색합니다.
# 리스트 컴프리헨션의 표현식을 사용하여 더 간결합니다.
# 초기 gen 값을 설정하고 반복문에서 찾았을 때 gen에 대입함으로써 못찾을 경우에 시간이 짧게 걸립니다.
## 성능
# 31120KB / 32ms
# N = int(input())

# gen = 0
# digit = len(str(N))

# for i in range(max(N - (9 * digit), 0), N):
#     n_string = str(i)
#     m = i + sum([int(j) for j in n_string])
#     if m == N:
#         gen = i
#         break

# print(gen)

## 리팩토링
import sys

n = int(sys.stdin.readline())
init = 0

for i in range(max(0, (n - (9 * len(str(n)))), n)):
    i_str = str(i)
    tmp = i + sum([int(j) for j in i_str])
    if tmp == n:
        init = i
        break
print(init)