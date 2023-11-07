section .data
section .bss
section .text
global main

main:
    ; Output a message
    mov edx, msg
    mov ecx, msglen
    mov ebx, 1
    mov eax, 4
    int 0x80

    ; Push flags onto the stack
    pushf

    ; Pop the flags into a register (e.g., EAX)
    pop eax

    ; Display the flags
    mov edx, eax
    mov ecx, 2
    mov ebx, 1
    mov eax, 4
    int 0x80

    ; Exit the program
    mov ebx, 0
    mov eax, 1
    int 0x80

section .data
msg db "Flags: ", 0
msglen equ $ - msg