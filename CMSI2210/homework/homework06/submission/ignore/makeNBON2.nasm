section .data
    input_values dd 0x12345678, 0xAABBCCDD, 0x11223344, 0x99887766, 0x55667788
    format db "Original number: 0x%x, Swapped number: 0x%x", 10, 0

section .text
    global _start
    extern makeNBO
    extern printf

_start:

    ; Call makeNBO with input = 0x12345678
    mov eax, [input_values]
    push eax
    call makeNBO
    add esp, 4

    ; Print the original and swapped number
    mov edx, eax
    push edx       ; swapped number
    push eax       ; original number
    push format
    call printf
    add esp, 12

    ; Call makeNBO with input = 0xAABBCCDD
    mov eax, [input_values + 4]
    push eax
    call makeNBO
    add esp, 4

    ; Print the original and swapped number
    mov edx, eax
    push edx       ; swapped number
    push eax       ; original number
    push format
    call printf
    add esp, 12

    ; Call makeNBO 3 more times with different inputs
    mov eax, [input_values + 8]
    push eax
    call makeNBO
    add esp, 4

    mov eax, [input_values + 12]
    push eax 
    call makeNBO
    add esp, 4

    mov eax, [input_values + 16]
    push eax
    call makeNBO 
    add esp, 4

    ; Exit
    mov eax, 0
    ret
