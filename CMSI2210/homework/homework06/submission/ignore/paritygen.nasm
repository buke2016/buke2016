section .data
    msg db "The parity bit is: ", 0
    one db 1
    zero db 0

section .text
    global _start

_start:
    mov eax, 0b10101110 ; Replace this with the byte of data you want to check
    mov ebx, 0
    mov ecx, 8

count_bits:
    shr eax, 1
    adc ebx, 0
    loop count_bits

    mov eax, 4
    mov ebx, 1
    mov ecx, msg
    mov edx, 18
    int 0x80

    cmp bl, 0
    je print_one
    jmp print_zero

print_one:
    mov eax, 4
    mov ebx, 1
    mov ecx, one
    mov edx, 1
    int 0x80
    jmp exit

print_zero:
    mov eax, 4
    mov ebx, 1
    mov ecx, zero
    mov edx, 1
    int 0x80

exit:section .data
    msg db "The parity bit is: ", 0
    one db 1
    zero db 0

section .text
    global _start

_start:
    mov eax, 0b10101110 ; Replace this with the byte of data you want to check
    mov ebx, 0
    mov ecx, 8

count_bits:
    shr eax, 1
    adc ebx, 0
    loop count_bits

    mov eax, 4
    mov ebx, 1
    mov ecx, msg
    mov edx, 18
    int 0x80

    cmp bl, 0
    je print_one
    jmp print_zero

print_one:
    mov eax, 4
    mov ebx, 1
    mov ecx, one
    mov edx, 1
    int 0x80
    jmp exit

print_zero:
    mov eax, 4
    mov ebx, 1
    mov ecx, zero
    mov edx, 1
    int 0x80

exit:
    mov eax, 1
    xor ebx, ebx
    int 0x80

    mov eax, 1
    xor ebx, ebx
    int 0x80
