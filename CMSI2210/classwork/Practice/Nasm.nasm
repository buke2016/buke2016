global   _main                ; This is the main entry point
extern   _printf              ; External code from the "C" library

section  .data                ; Data segment
    format db "%d", 0x0A, 0x00  ; Format string for printing a decimal number with a newline character

section  .text                ; Text (code) segment

_main:
    push    ebp                ; Save the base pointer
    mov     ebp, esp           ; Set up a new base pointer

    mov     ecx, 10            ; Number of powers of 2 to print
    xor     esi, esi            ; Clear ESI (used as the loop counter)

print_powers_of_two:
    push    esi                ; Save the current value of ESI on the stack
    mov     eax, esi           ; Move the loop counter (i) to EAX
    push    eax                ; Push the value to the stack
    push    format             ; Push the format string to the stack
    call    _printf            ; Call printf()
    add     esp, 8             ; Adjust the stack pointer

    pop     esi                ; Restore the loop counter from the stack

    inc     esi                ; Increment ESI (i)
    cmp     esi, ecx           ; Compare i to the number of powers to print (10)
    jl      print_powers_of_two  ; If i < 10, continue the loop

exit_program:
    mov     esp, ebp           ; Restore the stack pointer
    pop     ebp                ; Restore the base pointer
    ret                        ; Return to the operating system

section .data
message: db 'Hello, World', 0x0A, 0x00
