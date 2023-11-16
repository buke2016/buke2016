section .data
    word db "RACECAR", 0
    msg_palindrome db "Palindrome", 0
    msg_not_palindrome db "Not Palindrome", 0

section .bss
    left resb 1
    right resb 1

section .text
    global _start

_start:
    ; Get the length of the word
    mov esi, 0  ; esi will be used as an index from the left
    xor ecx, ecx  ; Clear ecx (will be used as a counter)

    ; Calculate the length of the string
calculate_length:
    mov al, [word + esi]
    cmp al, 0
    je check_palindrome
    inc esi
    inc ecx
    jmp calculate_length

check_palindrome:
    ; Initialize indices for comparison
    mov esi, 0            ; Left index
    mov edi, ecx - 1     ; Right index

compare_characters:
    ; Load characters from both ends
    mov al, [word + esi]
    mov bl, [word + edi]

    ; Compare characters
    cmp al, bl
    jne not_palindrome

    ; Move indices towards the center
    inc esi
    dec edi

    ; If left index is greater or equal to right index, it's a palindrome
    jae palindrome

    ; Continue comparing
    jmp compare_characters

palindrome:
    ; Display "Palindrome"
    mov eax, 4
    mov ebx, 1
    mov edx, msg_palindrome
    mov ecx, 10
    int 0x80

    ; Exit
    mov eax, 1
    int 0x80

not_palindrome:
    ; Display "Not Palindrome"
    mov eax, 4
    mov ebx, 1
    mov edx, msg_not_palindrome
    mov ecx, 15
    int 0x80

    ; Exit
    mov eax, 1
    int 0x80
