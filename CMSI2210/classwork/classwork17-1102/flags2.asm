section .data
    msg db "Flags register value: ", 0
    msg2 db "Carry flag set", 0
    msg3 db "Overflow flag set", 0

section .text
    global _start

_start:
    ; Output flags register value
    pushf
    pop rax
    mov rdi, msg
    mov rsi, rax
    mov rdx, 0
    call printf

    ; Add two numbers and output flags register value
    mov eax, 65535
    mov ebx, 1
    add eax, ebx
    pushf
    pop rax
    mov rdi, msg
    mov rsi, rax
    mov rdx, 0
    call printf