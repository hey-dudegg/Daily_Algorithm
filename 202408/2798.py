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