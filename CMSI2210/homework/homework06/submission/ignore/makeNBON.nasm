section .data
    input_values dd 12345678h, 87654321h, 11112222h, 33334444h, 55556666h  ; Different input values to test the function

section .text
    global _start

extern makeNBO  ; Extern declaration of the C function

_start:
    ; Call the C function makeNBO at least five times with different values to test it
    mov ecx, 5  ; Number of times to call the function
    mov esi, input_values  ; Address of the input values array

.loop:
    mov eax, [esi]  ; Load the input value into eax
    call makeNBO  ; Call the C function
    ; You can now use the swapped value in eax
    add esi, 4  ; Move to the next input value
    loop .loop  ; Repeat for the remaining values

    ; Exit the program
    mov eax, 1  ; Exit system call number
    xor ebx, ebx  ; Return 0 status
    int 80h  ; Call the kernel