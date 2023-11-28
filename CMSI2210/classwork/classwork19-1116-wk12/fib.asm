section .data
    output_format db "%lu ", 0 ; format for printing unsigned long
    newline db 0xA  ; newline character

section .text
    global _start

_start:
    ; Initialize variables
    mov eax, 0      ; num1 (previous)
    mov ebx, 1      ; num2 (current)
    mov ecx, 10     ; counter (number of Fibonacci numbers to generate)

    ; Print the first number (0)
    push eax        ; save registers before making a syscall
    mov eax, 4      ; syscall number for sys_write
    mov ebx, 1      ; file descriptor 1 is stdout
    mov ecx, output_format
    mov edx, 4      ; length of the string
    int 0x80        ; call kernel
    pop eax         ; restore registers after syscall

    ; Generate and print the rest of the Fibonacci numbers
    fibonacci_loop:
        ; Calculate the next Fibonacci number: temp = num1 + num2
        add eax, ebx  ; temp = num1 + num2

        ; Print the current Fibonacci number
        push eax      ; save registers before making a syscall
        mov eax, 4    ; syscall number for sys_write
        mov ebx, 1    ; file descriptor 1 is stdout
        mov ecx, eax  ; address of the variable to print
        mov edx, 4    ; length of the variable (4 bytes for unsigned long)
        int 0x80      ; call kernel
        pop eax       ; restore registers after syscall

        ; Print newline character
        push ebx      ; save registers before making a syscall
        mov eax, 4    ; syscall number for sys_write
        mov ebx, 1    ; file descriptor 1 is stdout
        mov ecx, newline
        mov edx, 1    ; length of the string
        int 0x80      ; call kernel
        pop ebx       ; restore registers after syscall

        ; Move num2 to num1 and temp to num2
        mov edx, ebx  ; save num2 in edx
        mov ebx, eax  ; num2 = temp
        mov eax, edx  ; num1 = num2

        ; Decrease the counter
        sub ecx, 1
        jnz fibonacci_loop ; jump to the loop if counter is not zero

    ; Exit the program
    mov eax, 1      ; syscall number for sys_exit
    xor ebx, ebx    ; exit code 0
    int 0x80        ; call kernel
