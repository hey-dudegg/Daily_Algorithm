#include "header2.h"
//#include "header1.h" // ��ȯ ���� ���� �ذ��� ���� header1.h�� ���⼭ ����

#include <stdio.h>

char* func2() {

    printf("%s \n", func1()); // func1�� ȣ������ �ʰ� printf�� ���
    char* ch2 = "header2.h �Դϴ�.";
    
    return ch2;
}
