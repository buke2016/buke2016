; findGCD.nasm - finds GCD of two numbers entered from stdin

global _start

section .text

_start:

    ; Read first number
    mov eax, 3 ; sys_read syscall number
    mov ebx, 0 ; stdin file descriptor 
    mov ecx, num1 ; put number here
    mov edx, 10 ; max number of bytes to read
    int 80h ; call kernel

    ; Read second number 
    mov eax, 3 ; sys_read syscall 
    mov ebx, 0 ; stdin
    mov ecx, num2 ; put number here 
    mov edx, 10 ; max bytes
    int 80h

    ; Move numbers into registers 
    mov eax, [num1]
    mov ebx, [num2]

gcd_loop:
    cmp ebx, 0
    je print ; if ebx=0, we're done
    cdq ; sign extend eax to edx:eax
    idiv ebx ; edx:eax / ebx -> rem in edx, quot in eax 
    mov eax, ebx ; copy ebx to eax for next iteration
    mov ebx, edx ; copy remainder to ebx
    jmp gcd_loop ; keep looping

print:
    ; Print GCD    
    mov eax, 4 ; sys_write syscall number
    mov ebx, 1 ; stdout file descriptor
    mov ecx, num1 ; put GCD here from eax
    mov edx, 10 ; max bytes to write 
    int 80h

    ; Exit 
    mov eax, 1 ; sys_exit syscall number 
    mov ebx, 0 ; exit code 0 
    int 80h 

section .bss
num1 resb 10 ; reserve 10 bytes 
num2 resb 10