global parity3

section .text
parity3:
	; Get the input byte from the first argument
	mov     dl, byte [esp + 4]

	; Initialize counter for number of ones
	mov     cl, 0

	; Loop through each bit in the byte
loop:
	; Check if the least significant bit is 1
	test    dl, 1

	; Increment counter if the bit is 1
	jz      next_bit
	inc     cl

next_bit:
	; Shift the byte right one bit
	shr     dl, 1

	; Repeat loop until all bits have been checked
	jnz     loop

	; Check if the number of ones is even
	test    cl, 1

	; Set parity bit to 1 if even, 0 if odd
	jz      set_parity_bit

	; Parity bit should be 0
	mov     al, 0
	jmp     done

set_parity_bit:
	; Parity bit should be 1
	mov     al, 1

done:
	; Return the parity bit in AL
	ret

section .data
msg_prompt db "Enter a byte: "
msg_odd db "Odd parity: "

section .bss
input_byte resb 1

section .text
main:
	; Print prompt
	mov     esi, offset msg_prompt
	call    puts

	; Read input byte
	mov     esi, offset input_byte
	mov     edi, 1
	call    read

	; Calculate and print odd parity bit
	push    dword input_byte[0]
	call    parity3
	add     esp, 4

	mov     esi, offset msg_odd
	call    puts

	mov     dl, al
	call    putchar

	mov     eax, 1
	int     0x80