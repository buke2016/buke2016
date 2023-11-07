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
    mov eax, 1
    mov ebx, 2
    add eax, ebx
    pushf
    pop rax
    mov rdi, msg
    mov rsi, rax
    mov rdx, 0
    call printf

    ; Loop until carry flag is set
    mov eax, 0
    mov ebx, 0
    mov ecx, 1
    mov edx, 1
    add eax, ecx
    add ebx, edx
    pushf
    pop rax
    jc carry_flag
    jmp loop

carry_flag:
    mov rdi, msg2
    mov rsi, 0
    mov rdx, 0
    call printf
    jmp exit

loop:
    add eax, ecx
    add ebx, edx
    pushf
    pop rax
    jc carry_flag
    jo overflow_flag
    jmp loop

overflow_flag:
    mov rdi, msg3
    mov rsi, 0
    mov rdx, 0
    call printf
    jmp exit

exit:
    mov eax, 0
    ret


# nasm -f win64 -d flags.exe