#include "header2.h"
//#include "header1.h" // 순환 참조 문제 해결을 위해 header1.h를 여기서 포함

#include <stdio.h>

char* func2() {

    printf("%s \n", func1()); // func1을 호출하지 않고 printf만 사용
    char* ch2 = "header2.h 입니다.";
    
    return ch2;
}
