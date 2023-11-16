section .data
    word db 'RACECAR'
    len equ $-word

section .text
    global _start

_start:
    mov esi, word
    mov edi, esi
    add edi, len
    dec edi

check:
    cmp esi, edi
    jge palindrome

    mov al, [esi]
    mov bl, [edi]
    cmp al, bl
    jne not_palindrome

    inc esi
    dec edi
    jmp check

palindrome:
    mov eax, 1
    mov ebx, 0
    int 0x80

not_palindrome:
    mov eax, 0
    mov ebx, 0
    int 0x80