/*
1085 직사각형에서 탈출
https://www.acmicpc.net/problem/1085

한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고,
왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다.
직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

풀이
1. int형 minimum 선언, 입력값 파싱
2. w-x, h-y, x, y 을 비교하여 최솟값 저장
3. 출력
*/

/* version 1
#include <stdio.h>
#include <string.h>

int main() {
	//char nums[4];
	int w, h, x, y, min;
	
	scanf_s("%d %d %d %d", &x, &y, &w, &h);
	
	min = w - x;
	
	if (min > x) {
		min = x;
	}
	if (min > h - y) {
		min = h - y;
	}
	if (min > y) {
		min = y;
	}

	printf("%d", min);

	return 0;
}
 */

/* version 2 */
#include <stdio.h>
#include <string.h>

int main() {
	int nums1[100] = { 0, };

	int min;

	fgets(nums1, 100, stdin);

	printf("%s\n", nums1);

	return 0;
}
