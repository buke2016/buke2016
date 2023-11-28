section .data
    value dd 1
    result dd 0

section .text
    global _start
    extern makeNBO

_start:
    ; Call makeNBO function
    mov eax, [value]
    call makeNBO

    ; Display the result
    mov eax, [result]
    mov ebx, 1         ; file descriptor: stdout
    mov ecx, eax       ; address of the result variable
    mov edx, 4         ; number of bytes to write
    mov eax, 4         ; syscall: sys_write
    int 0x80           ; interrupt to invoke the syscall

    ; Exit the program
    mov eax, 1         ; syscall: sys_exit
    xor ebx, ebx       ; exit code 0
    int 0x80           ; interrupt to invoke the syscall
