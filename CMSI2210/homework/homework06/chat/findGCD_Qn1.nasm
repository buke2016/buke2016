section .data
    num1 dd 0
    num2 dd 0
    result dd 0

section .text
    global _start

_start:
    ; Read the first number from stdin
    mov eax, 3          ; syscall: sys_read
    mov ebx, 0          ; file descriptor: stdin
    mov ecx, num1       ; buffer to read into
    mov edx, 4          ; number of bytes to read
    int 0x80            ; interrupt to invoke the syscall

    ; Convert the string to an integer (num1)
    mov eax, num1
    call str_to_int

    ; Read the second number from stdin
    mov eax, 3          ; syscall: sys_read
    mov ebx, 0          ; file descriptor: stdin
    mov ecx, num2       ; buffer to read into
    mov edx, 4          ; number of bytes to read
    int 0x80            ; interrupt to invoke the syscall

    ; Convert the string to an integer (num2)
    mov eax, num2
    call str_to_int

    ; Call the GCD function
    mov eax, num1
    mov ebx, num2
    call findGCD

    ; Convert the result to a string
    mov ebx, eax
    mov eax, result
    call int_to_str

    ; Write the result to stdout
    mov eax, 4          ; syscall: sys_write
    mov ebx, 1          ; file descriptor: stdout
    mov ecx, result     ; address of the result variable
    mov edx, 4          ; number of bytes to write
    int 0x80            ; interrupt to invoke the syscall

    ; Exit the program
    mov eax, 1          ; syscall: sys_exit
    xor ebx, ebx        ; exit code 0
    int 0x80            ; interrupt to invoke the syscall

; Function to convert a string to an integer
str_to_int:
    xor edx, edx        ; Clear edx to store the result
    mov ecx, 10         ; Set the divisor to 10
convert_loop:
    mov ebx, eax        ; Copy the current value of eax to ebx
    xor eax, eax        ; Clear eax to prepare for division
    div ecx             ; Divide ebx by 10, result in eax, remainder in edx
    add edx, '0'        ; Convert remainder to ASCII
    imul edx, 0x100     ; Shift ASCII digit to the left
    add edx, ebx        ; Add the ASCII digit to the result
    test eax, eax        ; Check if quotient is zero
    jnz convert_loop    ; If not, continue the loop
    mov eax, edx        ; Copy the result to eax
    ret

; Function to convert an integer to a string
int_to_str:
    mov ecx, 10          ; Set the divisor to 10
    xor edx, edx         ; Clear edx to store the reversed string
reverse_loop:
    div ecx              ; Divide eax by 10, result in eax, remainder in edx
    add dl, '0'          ; Convert remainder to ASCII
    mov [edx + result], dl ; Store the ASCII digit in the result buffer
    inc edx              ; Move to the next position in the buffer
    test eax, eax         ; Check if quotient is zero
    jnz reverse_loop     ; If not, continue the loop
    mov eax, result      ; Copy the address of the result buffer to eax
    call reverse_string  ; Reverse the string in place
    ret

; Function to reverse a null-terminated string in place
reverse_string:
    push eax             ; Save the address of the string
    xor ecx, ecx         ; Clear ecx (counter for string length)
count_length:
    cmp byte [eax + ecx], 0 ; Check for null terminator
    je  end_count        ; If found, jump to the end of the counting loop
    inc ecx             ; Increment the counter
    jmp count_length     ; Continue the counting loop
end_count:
    dec ecx             ; Decrement the counter (remove null terminator)
    mov edx, eax        ; Set edx to the address of the first character
    add edx, ecx        ; Move edx to the address of the last character
reverse_loop:
    cmp eax, edx        ; Check if we have reached the middle of the string
    jge end_reverse     ; If yes, jump to the end of the reverse loop
    mov al, [eax]       ; Load the current character from the beginning
    mov bl, [edx]       ; Load the current character from the end
    mov [eax], bl       ; Swap the characters
    mov [edx], al       ; Swap the characters
    inc eax             ; Move to the next character from the beginning
    dec edx             ; Move to the next character from the end
    jmp reverse_loop    ; Continue the reverse loop
end_reverse:
    pop eax              ; Restore the original address of the string
    ret

; Function to find the GCD of two numbers (Euclidean algorithm)
findGCD:
    .while:
        cmp eax, ebx
        jl .swap
        sub eax, ebx
        jmp .while
    .swap:
        xchg eax, ebx
        jmp .while
    ret
