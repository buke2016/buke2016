section .data
    input_values dd 0x12345678, 0xdeadbeef, 0xabcdef01, 0x87654321, 0xfaceb00c
    output_msg db "Original number: 0x%x, Swapped number: 0x%x", 10, 0

section .text
    extern printf, makeNBO
    global _start

_start:
    mov ecx, 5  ; Number of times to call makeNBO
    mov esi, input_values  ; Address of input values array
call_makeNBO:
    mov eax, [esi]  ; Load input value
    push eax  ; Prepare argument for makeNBO
    call makeNBO  ; Call makeNBO
    add esp, 4  ; Clean up the stack
    mov ebx, eax  ; Swapped number
    mov eax, [esi]  ; Original number
    push eax  ; Prepare original number for printing
    push ebx  ; Prepare swapped number for printing
    push output_msg  ; Format string
    call printf  ; Print the numbers
    add esp, 12  ; Clean up the stack
    add esi, 4  ; Move to the next input value
    loop call_makeNBO  ; Loop until ecx is zero

    ; Exit the program
    mov eax, 0  ; Syscall number for exit
    int 0x80  ; Call the kernel