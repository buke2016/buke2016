section .text
    global paritygen

paritygen:
    ; Input: al=byte to calculate parity
    ; Output: al=parity bit (odd parity)

    mov ah, 0    ; Clear high bits
    mov ecx, 8   ; Loop counter

parity_loop:
    shr al, 1    ; Shift right, moving the lowest bit to CF
    rcl ah, 1    ; Rotate through carry to the high bit
    loop parity_loop

    ; Parity bit is in the least significant bit of ah
    test ah, 1
    jz parity_even
    jmp parity_odd

parity_even:
    ; Set parity bit for even parity
    mov al, 0
    ret

parity_odd:
    ; Set parity bit for odd parity
    mov al, 1
    ret
