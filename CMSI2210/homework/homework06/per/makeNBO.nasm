section .data
    numbers dd 12345678, 87654321, 98765432, 23456789, 34567890

section .text
    global _start

_start:
    mov ecx, 5  ; Number of times to call makeNBO
    mov esi, numbers  ; Address of the array
.loop:
    mov eax, dword [esi]  ; Load the number
    call makeNBO  ; Call the C function
    ; Print the result
    mov ebx, eax  ; Move the result to EBX for printing
    mov eax, 4  ; sys_write
    mov edx, 4  ; Number of bytes to write
    int 0x80  ; Call kernel
    add esi, 4  ; Move to the next number
    loop .loop  ; Loop until ECX is 0

    ; Exit the program
    mov eax, 1  ; sys_exit
    xor ebx, ebx  ; Return 0
    int 0x80  ; Call kernel