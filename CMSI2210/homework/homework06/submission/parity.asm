
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
    mov     rcx, 0  ; Counter for set bits

    ; Bit counting loop
count_bits:
    test    al, 1
    jnz     increment_counter

    ; If bit is not set, continue to the next bit
    shr     al, 1
    jmp     check_end

increment_counter:
    inc     rcx

check_end:
    ; Check if all bits are processed
    cmp     al, 0
    jnz     count_bits

    ; Determine parity
    test    rcx, 1
    jz      even_parity

    ; Odd parity: Print 1
    mov     rdi, 1
    call    print_parity
    jmp     end_parity

even_parity:
    ; Even parity: Print 0
    mov     rdi, 0
    call    print_parity

end_parity:
    ; Function epilogue
    mov     rsp, rbp
    pop     rbp
    ret

print_parity:
    ; Use the value in rdi to determine what to print
    ; Use printf-style formatting

    ; Load the byte into rsi
    mov     rsi, rdi

    mov     rdi, format     ; Format string
    mov     rdx, 1          ; Length of the buffer
    mov     eax, 0          ; Clear upper bits of rax (avoid issues with printf)
    call    printf wrt ..plt ; Use the PLT (Procedure Linkage Table) for external function calls

    ret
