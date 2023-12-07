section .data
    prompt db "Enter a byte of data: ", 0
    result_msg db "Parity bit is: ", 0
    newline db 13, 10, 0  ; Carriage return (CR) and line feed (LF)
    one db '1', 0        ; String for '1'
    zero db '0', 0       ; String for '0'

section .bss
    input_byte resb 1
    parity resb 1

section .text
    global main

main:
    ; Print prompt
    mov eax, 4
    mov ebx, 1
    mov ecx, prompt
    mov edx, 24
    int 0x80

    ; Read input byte
    mov eax, 3
    mov ebx, 0
    mov ecx, input_byte
    mov edx, 1
    int 0x80

    ; Calculate parity
    movzx eax, byte [input_byte]
    mov ebx, 0  ; Counter for the number of 1s

    ; Loop to count 1s
    count_bits:
        test eax, 1
        jz next_bit
        inc ebx

    next_bit:
        shr eax, 1
        jnz count_bits

    ; Check odd or even parity
    test ebx, 1
    jz even_parity

    ; Odd parity: set 1
    mov byte [parity], '1'
    jmp print_result

even_parity:
    ; Even parity: set 0
    mov byte [parity], '0'

print_result:
    ; Print result message
    mov eax, 4
    mov ebx, 1
    mov ecx, result_msg
    mov edx, 16
    int 0x80

    ; Print parity bit
    mov eax, 4
    mov ebx, 1
    mov ecx, parity
    mov edx, 1
    int 0x80

    ; Print newline
    mov eax, 4
    mov ebx, 1
    mov ecx, newline
    mov edx, 3
    int 0x80

    ; Exit
    mov eax, 1
    xor ebx, ebx
    int 0x80
