section .data
    byte db 10101110b  ; Example byte of data

section .text
    global _start

_start:
    mov al, [byte]  ; Move the byte of data into the AL register
    xor ah, ah      ; Clear AH to ensure it doesn't affect the result
    mov bl, 1       ; Set BL to 1 for counting the number of 1 bits

count_bits:
    test al, bl     ; Test the lowest bit of AL
    jz bit_is_zero  ; Jump if the result is zero
    inc ah          ; Increment AH if the result is not zero

bit_is_zero:
    shl bl, 1       ; Shift BL left to test the next bit
    cmp bl, 0       ; Compare BL to 0 to check if all bits have been tested
    jne count_bits  ; Jump back to count_bits if not all bits have been tested

    test ah, 1      ; Test the number of 1 bits to determine odd or even
    jz print_parity ; Jump to print_parity if the number of 1 bits is even
    mov dl, '0'     ; Move '0' (odd parity) into DL
    jmp exit        ; Jump to exit

print_parity:
    mov dl, '1'     ; Move '1' (even parity) into DL

exit:
    mov ah, 2       ; Set AH to 2 for printing the result
    int 21h         ; Print the result
    mov ah, 4Ch     ; Set AH to 4Ch for exiting the program
    int 21h         ; Exit the program