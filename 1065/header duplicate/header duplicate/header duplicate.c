
#include <stdio.h>
#include <stdlib.h>

#include "header1.h"					// header1.h 선언
#include "header2.h"					// header2.h 선언

int main() {

	printf("%s \n", func1());	// header1.h 안에 정의되어 있는 함수 사용
	printf("%s \n", func2());	// header2.h 안에 정의되어 있는 함수 사용	

	system("pause");
	return 0;
}