###############################
## 백준 11816 8진수, 10진수, 16진수
# 정수 X가 주어진다. 정수 X는 항상 8진수, 10진수, 16진수 중에 하나이다.
# 8진수인 경우에는 수의 앞에 0이 주어지고, 16진수인 경우에는 0x가 주어진다.
# X를 10진수로 바꿔서 출력하는 프로그램을 작성하시오.
# import string
# import sys

# x = sys.stdin.readline()

# # if int(x) < 8:                # 예외사항(x가 8이하인 경우)
# #     print(x)
# #     exit()

# if x[0] == '0' :                # 10진수가 아닐 때
#     if x[1] == 'x' :            # 16진수의 경우
#         x = int(x, 16)
#         # for i in range(len(x) - 1, 2) :
#         #     sum += (int(x[i]) * (8 ** cnt))
#         #     cnt += 1
#     else :                      # 8진수의 경우
#         x = int(x, 8)
#         # for i in range(len(x) - 1, 1) :
#         #     sum += (int(x[i]) * (16 ** cnt))
#         #     cnt += 1
# else :                          # 10진수일 때
#     x = int(x)

# print(x)

####################################
# 다른 사람 코드
try : n = eval(s := input())
except : n = int(s, 8)
print(n)