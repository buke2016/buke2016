section .data
    input_values dd 0x12345678, 0xdeadbeef, 0xabcdef01, 0x87654321, 0xfaceb00c
    output_msg db "Original number: 0x%x, Swapped number: 0x%x", 10, 0

section .text
    extern makeNBO
    extern GetStdHandle
    extern WriteConsoleA
    extern ExitProcess

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

        ; Prepare original and swapped numbers for printing
        push ebx
        push eax
        ; Prepare format string
        push output_msg
        ; Write to the console
        call print_to_console
        add esp, 12  ; Clean up the stack
        add esi, 4  ; Move to the next input value
        loop call_makeNBO  ; Loop until ecx is zero

    ; Exit the program
    push 0
    call ExitProcess

print_to_console:
    ; Arguments: LPVOID lpBuffer, DWORD nNumberOfCharsToWrite, LPDWORD lpNumberOfCharsWritten, LPVOID lpReserved, LPVOID lpReserved
    ; WriteConsoleA arguments: HANDLE hConsoleOutput, const VOID *lpBuffer, DWORD nNumberOfCharsToWrite, LPDWORD lpNumberOfCharsWritten, LPVOID lpReserved
    mov eax, -11 ; GetStdHandle argument for STDOUT
    call GetStdHandle
    mov edi, eax ; Store the handle in edi
    mov eax, edi ; Move handle to eax for WriteConsoleA
    lea ecx, [esp + 4] ; Pointer to the buffer
    lea edx, [esp + 8] ; Pointer to the length
    push 0 ; Reserved parameter
    push 0 ; Reserved parameter
    push eax ; Handle to console
    call WriteConsoleA
    ret
