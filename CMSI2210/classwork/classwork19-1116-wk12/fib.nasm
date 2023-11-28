section .data
format db '%10d', 0x0A, 0x00  ; Format string for printf
newline db 0x0A, 0x00           ; Newline character

section .text
global _main
extern _printf

_main:
    push EBX                  ; Save EBX since we use it

    mov ECX, 0x14             ; ECX will countdown from 20 to 0
    xor EAX, EAX              ; EAX will hold the current number
    xor EBX, EBX              ; EBX will hold the next number
    inc EBX                   ; EBX is originally 1

print:
    push EAX                  ; Save EAX
    push ECX                  ; Save ECX

    push EAX                  ; Push EAX for the call to printf()
    push format               ; Push the format statement
    call _printf              ; Call the printf function from "C"
    add ESP, 8                ; Restore the stack pointer

    push EAX                  ; Save EAX for the second printf call
    push newline              ; Push the newline character
    call _printf              ; Call printf for the newline
    add ESP, 8                ; Restore the stack pointer

    pop ECX                   ; Restore the value of ECX
    pop EAX                   ; Restore the value of EAX

    mov EDX, EAX              ; Save the current number
    mov EAX, EBX              ; Set the next number as the current one
    add EBX, EDX              ; Calculate the new next number
    dec ECX                   ; Count down
    jnz print                 ; If not done counting, repeat the loop

    pop EBX                   ; Restore EBX before returning
    ret

section .data
format db '%10d', 0x00
newline db 0x0A, 0x00
