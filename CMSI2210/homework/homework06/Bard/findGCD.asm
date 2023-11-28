global _findGCD

section .text

_findGCD:
    mov eax, ebx ; ebx contains the first number
    mov ecx, edx ; edx contains the second number

    loop:
        mov eax, ebx
        xor edx, edx
        div ecx
        mov ebx, edx

        cmp ebx, 0
        jne loop

    ret

section .data
