#include <stdio.h>

void main()
{
    unsigned int intArray[] = {12,24,3};
    int num = sizeof(intArray) / sizeof(intArray[0]);
    unsigned int MCD;

    __asm
    {
        xor ebx,ebx
        xor edx,edx
        xor eax,eax
        mov eax, intArray[0]
        mov ebx, intArray[1]
        jmp major

    zerob:
        mov MCD, eax
        jmp fine

    major:
        cmp eax,ebx
        jg nextstep
        xchg eax,ebx
        jmp major

    nextstep:
        cmp ebx,0
        je zerob
        jne modulus

    modulus:
        div ebx
        mov MCD,edx
        mov eax,ebx
        mov ebx,MCD
        jmp nextstep

    fine:

    }

    printf("M.C.D.: %d \n", MCD);
    getchar();
}