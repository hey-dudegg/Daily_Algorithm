##############################
## 11728 백준 배열 합치기
# 정렬되어 있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

## 풀이
# 출력값을 보아 합친 뒤 정렬해주면 될 것 같다.
##############################
# n, m = input().split()
# num = list(map(int, input().split()))
# mum = list(map(int, input().split()))

# sum = num + mum
# sum.sort()              # sum = sum.sort()로 해서 sum이 자꾸 none이 나왔음
# ans = ' '.join(map(str, sum))
# print(ans)

# 304400	1136	Python 3 / 수정	241
## 다른 사람
# 305508	780	Python 3 / 수정	197
import sys
input = sys.stdin.readline

def solution():
    input()
    a = input()
    b = input()
    print(" ".join(sorted((a + b).split(), key = int)))

if __name__ == "__main__":
    solution()
