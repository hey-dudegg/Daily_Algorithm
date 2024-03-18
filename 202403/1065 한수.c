/*
백준 1065 한수
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를
출력하는 프로그램을 작성하라.

풀이
N은 세 자리 수 일 때 문제가 생긴다.
세 자릿수를 파싱해서 리스트에 담는다.
0번째 요소와 1번째 요소의 차이가 1~2의 자리와 같다면 cnt++

---실패

*/
//
//#include <stdio.h>
//
//void main() {
//	int num, tmp1, tmp2;
//	int cnt = 99;
//	int num_list[4] = {0, };
//
//	scanf_s("%d", &num);
//
//	for (int i = 100; i <= num; i++) {
//		for (int j = 2; j >= 0; j--) {
//			tmp1 = i;
//			tmp2 = tmp1 % 10;
//			tmp1 = tmp1 / 10;
//			num_list[j] = tmp2;
//			printf("%d", num_list[j]);
//		}
//		printf("\n");
//	}
//}

/* 솔루션 */
#include <stdio.h>

int chk(int n){
	int n1 = n % 10;
	int n2 = (n / 10) % 10;
	int n3 = (n / 100) % 10;

	if (n2 * 2 == n1 + n3) return 1;
	return 0;
}

void main() {
	int n;
	int ret;

	scanf_s("%d", &n);

	if (n < 100) ret = n;
	
	else {
		ret = 99;
		
		if (n == 1000) n = 999;

		for (int i = 100; i <= n; i++) {
			ret += chk(i);
		}
	}

	printf("%d\n", ret);
}
