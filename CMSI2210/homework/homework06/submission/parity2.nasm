; parity.asm

section .data
    format db "Parity Bit: %d", 10, 0  ; Format string for printing

section .text
    bits 64 ; Specify 64-bit mode
    global paritygen
    extern printf

paritygen:
    ; Function prologue
    push    rbp
    mov     rbp, rsp
    sub     rsp, 16  ; Adjust stack if needed

    ; Initialize counters
    mov     r8, 0  ; Counter for set bits

    ; Bit counting loop
count_bits:
    test    al, 1
    jnz     increment_counter

    ; If bit is not set, continue to the next bit
    shr     al, 1
    jmp     check_end

increment_counter:
    inc     r8

check_end:
    test    al, al
    jnz     count_bits

    ; Parity calculation
    mov     rax, r8
    and     rax, 1  ; Check if the number of set bits is odd

    ; Print result
    mov     rdi, format
    mov     rsi, rax
    call    printf

    ; Function epilogue
    leave
    ret
