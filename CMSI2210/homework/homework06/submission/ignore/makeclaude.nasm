extern makeNBO
global main 

section .text
main:

    ; Call makeNBO with input = 0x12345678 
    mov eax, 0x12345678
    push eax
    call makeNBO
    add esp, 4

    ; Print the original and swapped number 
    mov edx, eax
    push input     ; original number
    push edx       ; swapped number
    push format
    call printf
    add esp, 12

    ; Call makeNBO with input = 0xAABBCCDD
    mov eax, 0xAABBCCDD
    push eax
    call makeNBO
    add esp, 4

    ; Print the original and swapped number
    mov edx, eax
    push input     ; original number  
    push edx       ; swapped number
    push format 
    call printf
    add esp, 12

    ; Call makeNBO 3 more times with different inputs
    mov eax, 0x11223344 
    push eax
    call makeNBO
    add esp, 4

    mov eax, 0x99887766
    push eax 
    call makeNBO
    add esp, 4

    mov eax, 0x55667788
    push eax
    call makeNBO 
    add esp, 4

    ; Exit
    mov eax, 0
    ret

section .data
input: dd 0
format: db "Original number: 0x%x, Swapped number: 0x%x", 10, 0